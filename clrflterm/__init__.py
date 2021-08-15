from sys import stdout
from typing import Union

from .ansi import (
    Styles,
    Foreground,
    Backgrounds,
)


def rprint(
        text: str,
        *,
        foreground: Union[Foreground, str] = "",
        style: Union[Styles, str] = "",
        background: Union[Backgrounds, str] = ""
) -> None:
    stdout.write(foreground + style + background + text + Styles.RESET + "\n")


def reset() -> None:
    stdout.write(Styles.RESET.value)
