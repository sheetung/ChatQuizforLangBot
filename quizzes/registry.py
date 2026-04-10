from __future__ import annotations

from quizzes.base import BaseQuiz
from quizzes.sbit import SbitQuiz


QUIZ_REGISTRY: dict[str, BaseQuiz] = {
    "sbit": SbitQuiz(),
}


def get_quiz(key: str) -> BaseQuiz | None:
    return QUIZ_REGISTRY.get(key.lower())
