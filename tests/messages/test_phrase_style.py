import unittest

from clrfterm.messages import PhraseStyle
from clrfterm.ansi import Background, Foreground, Style


class TestPhraseStyle(unittest.TestCase):
    def test_set_foreground(self) -> None:
        for foreground in Foreground:
            self.assertEqual(
                PhraseStyle().set_foreground(foreground),
                Style.RESET + foreground + Background.RESET
            )

    def test_set_background(self) -> None:
        for background in Background:
            self.assertEqual(
                PhraseStyle().set_background(background),
                Style.RESET + Foreground.RESET + background
            )

    def test_set_style(self) -> None:
        for style in Style:
            self.assertEqual(
                PhraseStyle().set_style(style),
                style + Foreground.RESET + Background.RESET
            )
