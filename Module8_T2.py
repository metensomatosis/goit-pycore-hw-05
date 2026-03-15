import re
from typing import Callable, Generator


def generator_numbers(text: str) -> Generator[float, None, None]:
    """
    Повертає генератор дійсних чисел, знайдених у тексті.
    Числа мають бути відокремлені пробілами або знаками пунктуації.
    """
    pattern: str = r"\b\d+\.\d+\b"

    for match in re.finditer(pattern, text):
        yield float(match.group())


def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    """
    Обчислює загальну суму всіх чисел, які повертає функція-генератор.
