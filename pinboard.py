from typing import Dict


class Pinboard(object):
    def __init__(self) -> None:
        self.max_size = 10
        self.size = 0
        self.mapping: Dict[str, str] = {}

    def add_plug(self, char_a: str, char_b: str) -> None:
        if (self.size == self.max_size):
            raise Exception("Pinboard is full")

        if (char_a in self.mapping):
            raise Exception("Plug already exists")

        if (char_b in self.mapping):
            raise Exception("Plug already exists")

        self.mapping[char_a] = char_b
        self.mapping[char_b] = char_a
        self.size += 1

    def remove_plug(self, char: str) -> None:
        if (char not in self.mapping):
            raise Exception("Plug does not exist")

        del self.mapping[self.mapping[char]]
        del self.mapping[char]
        self.size -= 1
