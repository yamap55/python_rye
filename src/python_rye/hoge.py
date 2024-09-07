"""sample"""

from logging import getLogger

logger = getLogger(__name__)


class Hoge:
    """
    Hoge class
    """

    def piyo(self) -> str:
        logger.info("piyo")
        return "piyo"
