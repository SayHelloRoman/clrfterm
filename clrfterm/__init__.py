__version__ = "1.0.5"

from sys import stdout
from typing import Union

from clrfterm.ansi import (
    Style,
    Foreground,
    Background,
)
from clrfterm.win import enable_ansi


def rprint(
        text: str,
        *,
        foreground: Union[Foreground, str] = "",
        style: Union[Style, str] = "",
        background: Union[Background, str] = ""
) -> None:
    """
    stdout.write auto-reset wrapper
    """
    stdout.write(foreground + style + background + text + Style.RESET_ALL + "\n")


def reset() -> None:
    """
    function reset
    """
    stdout.write(Style.RESET_ALL.value)
