import enum


class Level(enum.Enum):
    CRITICAL = 70
    DEBUG = 40
    ERROR = 60
    FATAL = 80
    INFO = 30
    NOTICE = 20
    TRACE = 10
    WARNING = 50
    UNSET = 0


class LevelColors(str, enum.Enum):
    CRITICAL = "\x1b[38;5;196m"
    DEBUG = "\x1b[38;5;32m"
    ERROR = "\x1b[38;5;202m"
    FATAL = "\x1b[38;5;198m"
    INFO = "\x1b[38;5;12m"
    NOTICE = "\x1b[38;5;15m"
    TRACE = "\x1b[38;5;44m"
    WARNING = "\x1b[38;5;220m"
    UNSET = "\x1b[0m"
