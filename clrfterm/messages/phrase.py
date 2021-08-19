from typing import Optional, Union

from clrfterm.ansi import Style
from clrfterm.messages.phrase_style import PhraseStyle


class Phrase(str):
    def __new__(
        cls,
        text: str = "",
        *,
        message_part_style: Optional[Union[PhraseStyle, str]] = None
    ) -> "Phrase":
        if message_part_style is None:
            message_part_style = PhraseStyle.Empty
        obj = super(Phrase, cls).__new__(cls, message_part_style + text + Style.RESET)
        obj.__text = text
        obj.__style = message_part_style
        return obj

    def set_text(self, text: str) -> "Phrase":
        return Phrase(text, message_part_style=self.__style)

    def set_style(self, style: Union[PhraseStyle, str]) -> "Phrase":
        return Phrase(self.__text, message_part_style=style)
