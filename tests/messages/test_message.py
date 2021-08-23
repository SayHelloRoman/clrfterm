import unittest

from clrfterm.ansi import Background, Foreground, Style
from clrfterm.messages import Phrase, Message


class TestMessage(unittest.TestCase):
    def test_add(self) -> None:
        self.assertEqual(
            Message()
                .add(Phrase("some phrase"))
                .add(Phrase("another phrase")), 

            Style.RESET + Foreground.RESET + Background.RESET 
            + "some phrase" + Style.RESET

            + Style.RESET + Foreground.RESET + Background.RESET 
            + "another phrase" + Style.RESET
        )
