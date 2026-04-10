from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class QuizQuestion:
    id: str
    text: str
    options: list[dict[str, Any]]
    dim: str | None = None
    special: bool = False
    kind: str | None = None


class BaseQuiz(ABC):
    key: str
    title: str

    @abstractmethod
    def build_questions(self) -> list[QuizQuestion]:
        raise NotImplementedError

    @abstractmethod
    def render_intro(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def render_result(self, answers: dict[str, int]) -> str:
        raise NotImplementedError

    def parse_answer(self, message_text: str, question: QuizQuestion) -> int | None:
        normalized = message_text.strip().upper()
        option_count = len(question.options)
        code_map = {"A": 1, "B": 2, "C": 3, "D": 4}
        if normalized in code_map and code_map[normalized] <= option_count:
            return question.options[code_map[normalized] - 1]["value"]
        if normalized.isdigit():
            index = int(normalized)
            if 1 <= index <= option_count:
                return question.options[index - 1]["value"]
        for option in question.options:
            if message_text.strip() == option["label"]:
                return option["value"]
        return None

    def apply_answer(
        self,
        questions: list[QuizQuestion],
        answers: dict[str, int],
        current_index: int,
        answer_value: int,
    ) -> tuple[list[QuizQuestion], dict[str, int], int]:
        updated_answers = dict(answers)
        updated_answers[questions[current_index].id] = answer_value
        return questions, updated_answers, current_index + 1

    def render_question(self, question: QuizQuestion, index: int, total: int) -> str:
        lines = [
            f"{self.title} 进行中 {index}/{total}",
            f"第 {index} 题：{question.text}",
            "",
        ]
        option_codes = ["A", "B", "C", "D"]
        for idx, option in enumerate(question.options):
            lines.append(f"{option_codes[idx]}. {option['label']}")
        lines.extend(
            [
                "",
                "请直接回复 A/B/C/D 或 1/2/3/4。",
                f"回复 `/测试 {self.key}` 可重新开始，回复 `取消` 可结束当前测试。",
            ]
        )
        return "\n".join(lines)
