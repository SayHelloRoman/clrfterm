import ctypes
import platform
from typing import Optional, NoReturn

from clrfterm.error import PlatformError


def enable_ansi() -> None:
    """
    This is for those who use cmd,
    windows does not support ansi sequences,
    but I found a way to fix it
    """

    if platform.system() != "Windows":
        raise PlatformError("This function is for windows only")

    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
