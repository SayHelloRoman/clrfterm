import unittest

from clrfterm.ansi import Background, Foreground, Style
from clrfterm.messages import Phrase, PhraseStyle


class TestPhrase(unittest.TestCase):
    def test_set_text(self) -> None:
        self.assertEqual(
            Phrase().set_text('some text'),
            Style.RESET + Foreground.RESET + Background.RESET 
            + 'some text' + Style.RESET
        )

    def test_set_style(self) -> None:
        self.assertEqual(
            Phrase("").set_style(
                PhraseStyle()
                    .set_foreground(Foreground.RED)
                    .set_background(Background.MAGENTA)
                    .set_style(Style.BOLD)
            ),
            Style.BOLD + Foreground.RED + Background.MAGENTA + Style.RESET
        )
