"""sample"""

from logging import getLogger

logger = getLogger(__name__)


class Hoge:
    """
    Hoge class
    """

    def piyo(self) -> str:
        """return piyo"""
        logger.info("piyo")
        return "piyo"


def add_numbers(a: int, b: int) -> int:
    """Add"""
    error_point = "error"
    return a + b


# pyright check error
result = add_numbers(10, "20")
