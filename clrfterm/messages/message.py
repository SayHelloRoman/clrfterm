from typing import Union

from clrfterm.messages.phrase import Phrase


class Message(str):
    def __new__(cls, *phrases: Union[Phrase, str]) -> "Message":
        obj = super(Message, cls).__new__(cls, ''.join(phrases))
        obj.__phrases = phrases
        return obj

    def add(self, phrase: Union[Phrase, str]) -> "Message":
        return Message(*self.__phrases, phrase)
