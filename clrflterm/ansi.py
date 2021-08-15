from enum import Enum


class Foreground(str, Enum):
    BLACK         = "\033[30m"
    RED           = "\033[31m"
    GREEN         = "\033[32m"
    YELLOW        = "\033[33m"
    BLUE          = "\033[34m"
    MAGENTA       = "\033[35m"
    CYAN          = "\033[36m"
    WHITE         = "\033[37m"


class Backgrounds(str, Enum):
    BLACK         = "\033[40m"
    RED           = "\033[41m"
    GREEN         = "\033[42m"
    YELLOW        = "\033[43m"
    BLUE          = "\033[44m"
    MAGENTA       = "\033[45m"
    CYAN          = "\033[46m"
    WHITE         = "\033[47m"


class Styles(str, Enum):
    BOLD          = "\033[1m"
    UNDERLINE     = "\033[4m"
    RESET         = "\033[0m"
