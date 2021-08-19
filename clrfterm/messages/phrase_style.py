from clrfterm.ansi import Foreground, Background, Style


class PhraseStyle(str):
    Empty = Style.RESET + Foreground.RESET + Background.RESET
    
    def __new__(
        cls,
        *,
        foreground: Foreground = Foreground.RESET, 
        background: Background = Background.RESET, 
        style: Style = Style.RESET,
    ) -> "PhraseStyle":
        obj = super(PhraseStyle, cls).__new__(cls, style + foreground + background)
        obj.__foreground = foreground
        obj.__background = background
        obj.__style = style
        return obj

    def set_foreground(self, foreground: Foreground) -> "PhraseStyle":
        return PhraseStyle(
            foreground=foreground,
            background=self.__background,
            style=self.__style,
        )

    def set_background(self, background: Background) -> "PhraseStyle":
        return PhraseStyle(
            foreground=self.__foreground,
            background=background,
            style=self.__style,
        )

    def set_style(self, style: Style) -> "PhraseStyle":
        return PhraseStyle(
            foreground=self.__foreground,
            background=self.__background,
            style=style,
        )
