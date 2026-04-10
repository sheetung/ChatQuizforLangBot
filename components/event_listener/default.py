from __future__ import annotations

import logging
import os
import sys
from dataclasses import dataclass, field

from langbot_plugin.api.definition.components.common.event_listener import EventListener
from langbot_plugin.api.entities import context, events
from langbot_plugin.api.entities.builtin.platform import message as platform_message

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from quizzes.base import BaseQuiz, QuizQuestion
from quizzes.registry import QUIZ_REGISTRY, get_quiz


logger = logging.getLogger(__name__)


@dataclass
class QuizSession:
    quiz: BaseQuiz
    questions: list[QuizQuestion]
    answers: dict[str, int] = field(default_factory=dict)
    current_index: int = 0


class DefaultEventListener(EventListener):
    def __init__(self) -> None:
        super().__init__()
        self.sessions: dict[str, QuizSession] = {}

    async def initialize(self):
        await super().initialize()

        @self.handler(events.PersonMessageReceived)
        async def handle_private_message(event_context: context.EventContext):
            message_text = self._extract_text(event_context).strip()
            if not message_text:
                return

            sender_id = str(event_context.event.sender_id)

            if message_text.startswith("/测试"):
                event_context.prevent_default()
                await self._handle_test_command(event_context, sender_id, message_text)
                return

            session = self.sessions.get(sender_id)
            if session is None:
                return

            event_context.prevent_default()
            if message_text in {"取消", "退出", "结束"}:
                self.sessions.pop(sender_id, None)
                await self._reply_text(
                    event_context,
                    "当前测试已结束。想重新开始的话，私聊发送 `/测试 <名称>` 即可。",
                )
                return

            current_question = session.questions[session.current_index]
            answer_value = session.quiz.parse_answer(message_text, current_question)
            if answer_value is None:
                await self._reply_text(
                    event_context,
                    "这题请直接回复 A/B/C/D 或 1/2/3/4。回复 `取消` 可结束当前测试。",
                )
                return

            session.questions, session.answers, session.current_index = session.quiz.apply_answer(
                session.questions,
                session.answers,
                session.current_index,
                answer_value,
            )

            if session.current_index >= len(session.questions):
                result_text = session.quiz.render_result(session.answers)
                self.sessions.pop(sender_id, None)
                await self._reply_text(event_context, result_text)
                return

            await self._send_current_question(event_context, session)

    async def _handle_test_command(
        self,
        event_context: context.EventContext,
        sender_id: str,
        message_text: str,
    ) -> None:
        parts = message_text.split(maxsplit=1)
        if len(parts) == 1:
            available = ", ".join(sorted(QUIZ_REGISTRY.keys()))
            await self._reply_text(
                event_context,
                f"请使用 `/测试 名称` 来启动测试。\n当前可用测试：{available}",
            )
            return

        quiz_key = parts[1].strip()
        quiz = get_quiz(quiz_key)
        if quiz is None:
            available = ", ".join(sorted(QUIZ_REGISTRY.keys()))
            await self._reply_text(
                event_context,
                f"未找到测试 `{quiz_key}`。\n当前可用测试：{available}",
            )
            return

        session = QuizSession(quiz=quiz, questions=quiz.build_questions())
        self.sessions[sender_id] = session
        await self._reply_text(event_context, quiz.render_intro())
        await self._send_current_question(event_context, session)

    async def _send_current_question(
        self,
        event_context: context.EventContext,
        session: QuizSession,
    ) -> None:
        question = session.questions[session.current_index]
        text = session.quiz.render_question(
            question,
            session.current_index + 1,
            len(session.questions),
        )
        await self._reply_text(event_context, text)

    def _extract_text(self, event_context: context.EventContext) -> str:
        message_chain = event_context.event.message_chain
        plain_texts = [
            element.text
            for element in message_chain
            if isinstance(element, platform_message.Plain)
        ]
        if plain_texts:
            return "".join(plain_texts)
        return str(message_chain)

    async def _reply_text(self, event_context: context.EventContext, text: str) -> None:
        await event_context.reply(
            platform_message.MessageChain([platform_message.Plain(text=text)])
        )
