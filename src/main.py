"""main"""

from logging import config

from python_rye.hoge import Hoge

config.fileConfig("logging.conf", disable_existing_loggers=False)

if __name__ == "__main__":
    Hoge().piyo()
