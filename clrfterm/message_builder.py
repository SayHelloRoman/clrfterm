from typing import Union

from .ansi import (
    Styles,
    Foreground,
    Backgrounds,
)


class MessageBuilder:
    def __init__(self):
        self.__text = ""
        self.__foreground = ""
        self.__background = ""
        self.__style = ""
        self.__reset = ""

    def __str__(self) -> str:
        return (
            self.__foreground
            + self.__style
            + self.__background
            + self.__text
            + self.__reset
        )

    def set_text(self, text: str) -> "MessageBuilder":
        self.__text = text
        return self

    def set_foreground(self, fg: Foreground) -> "MessageBuilder":
        self.__foreground = fg
        return self

    def set_background(self, bg: Backgrounds) -> "MessageBuilder":
        self.__background = bg
        return self

    def set_style(self, st: Styles) -> "MessageBuilder":
        self.__style = st
        return self

    def set_reset(self, reset: bool) -> "MessageBuilder":
        self.__reset = Styles.RESET if reset else ""
        return self
