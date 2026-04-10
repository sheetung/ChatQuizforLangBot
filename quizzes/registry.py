from __future__ import annotations

from quizzes.base import BaseQuiz
from quizzes.sbti import SbtiQuiz


QUIZ_REGISTRY: dict[str, BaseQuiz] = {
    "sbti": SbtiQuiz(),
}


def get_quiz(key: str) -> BaseQuiz | None:
    return QUIZ_REGISTRY.get(key.lower())
