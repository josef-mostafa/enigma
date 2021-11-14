from typing import Dict

from datastructs import Array


class Plugboard(object):
    def __init__(self) -> None:
        self.max_plugs = 10
        self.size = 0
        self.mapping: Dict[str, str] = {}
        self.pairs: Array = Array(self.max_plugs)

    def __repr__(self) -> str:
        return "\n".join([f"{i+1}: {self.pairs.get(i)[0]} <=> {self.pairs.get(i)[1]}" for i in range(self.size)])

    def reset(self) -> None:
        """
            Removes all plugs from the plugboard.
        """
        self.size = 0
        self.mapping = {}
        self.pairs = []

    def add_plug(self, char_a: str, char_b: str) -> None:
        """
            Adds a plug to the plugboard.
        """
        if (self.size == self.max_plugs):
            raise Exception("Plugboard is full")

        if (char_a in self.mapping):
            raise Exception("Plug already exists")

        if (char_b in self.mapping):
            raise Exception("Plug already exists")

        self.pairs.insert((char_a, char_b))

        self.mapping[char_a] = char_b
        self.mapping[char_b] = char_a
        self.size += 1

    def remove_plug(self, char: str) -> None:
        """
            Removes a plug from the plugboard.
        """
        if (char not in self.mapping):
            raise Exception("Plug does not exist")

        if self.pairs.contains((char, self.mapping[char])):
            self.pairs.remove((char, self.mapping[char]))

        if self.pairs.contains((self.mapping[char], char)):
            self.pairs.remove((self.mapping[char], char))

        del self.mapping[self.mapping[char]]
        del self.mapping[char]
        self.size -= 1

    def encrypt(self, plaintext: str) -> str:
        """
            Encrypts a plaintext string using the plugboard.
        """
        return "".join([self.mapping.get(char, char) for char in plaintext])
