import enum
from typing import Dict, List, Tuple


class Plugboard(object):
    def __init__(self) -> None:
        self.max_plugs = 10
        self.size = 0
        self.mapping: Dict[str, str] = {}
        self.pairs: List[Tuple[str, str]] = []

    def __repr__(self) -> str:
        return "\n".join(map(lambda x: f"{x[0]}: {x[1][0]} <=> {x[1][1]}", enumerate(self.pairs, 1)))

    def reset(self) -> None:
        self.size = 0
        self.mapping = {}
        self.pairs = []

    def add_plug(self, char_a: str, char_b: str) -> None:
        if (self.size == self.max_plugs):
            raise Exception("Plugboard is full")

        if (char_a in self.mapping):
            raise Exception("Plug already exists")

        if (char_b in self.mapping):
            raise Exception("Plug already exists")

        self.pairs.append((char_a, char_b))

        self.mapping[char_a] = char_b
        self.mapping[char_b] = char_a
        self.size += 1

    def remove_plug(self, char: str) -> None:
        if (char not in self.mapping):
            raise Exception("Plug does not exist")

        if (char, self.mapping[char]) in self.pairs:
            self.pairs.remove((char, self.mapping[char]))

        if (self.mapping[char], char) in self.pairs:
            self.pairs.remove((self.mapping[char], char))

        del self.mapping[self.mapping[char]]
        del self.mapping[char]
        self.size -= 1

    def encrypt(self, plaintext: str) -> str:
        return "".join([self.mapping.get(char, char) for char in plaintext])
