#!/usr/bin/env python3


class MyString:
    def __init__(self, value=""):
        self._value = ""
        self.value = value  # Use the setter for initial value assignment

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, str):
            print("The value must be a string.")
        else:
            self._value = new_value

    def is_sentence(self):
        return self._value.endswith(".")

    def is_question(self):
        return self._value.endswith("?")

    def is_exclamation(self):
        return self._value.endswith("!")

    def count_sentences(self):
        import re
        # Find sequences of characters that end in . ! or ? and are followed by a space or end of string
        sentences = re.findall(r'\b[^.!?]*[.!?](?=\s|$)', self._value)
        return len(sentences)

