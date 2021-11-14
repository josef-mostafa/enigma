from typing import Dict

from datastructs import Array, Map
from mappings import Mapping


class Plugboard(object):
    def __init__(self) -> None:
        self.max_plugs = 10
        self.size = 0
        self.mapping: Map = Map(self.max_plugs * 2)
        self.pairs: Array = Array(self.max_plugs)

    def __repr__(self) -> str:
        return "\n".join([f"{i+1}: {self.pairs.get(i)[0]} <=> {self.pairs.get(i)[1]}" for i in range(self.size)])

    def reset(self) -> None:
        """
            Removes all plugs from the plugboard.
        """
        self.size = 0
        self.mapping = Map(self.max_plugs * 2)
        self.pairs = Array(self.max_plugs)

    def add_plug(self, char_a: str, char_b: str) -> None:
        """
            Adds a plug to the plugboard.
        """
        if (self.size == self.max_plugs):
            raise Exception("Plugboard is full")

        if (self.mapping.contains(char_a)):
            raise Exception("Plug already exists")

        if (self.mapping.contains(char_b)):
            raise Exception("Plug already exists")

        self.pairs.insert((char_a, char_b))

        self.mapping.insert(char_a, char_b)
        self.mapping.insert(char_b, char_a)
        self.size += 1

    def remove_plug(self, char: str) -> None:
        """
            Removes a plug from the plugboard.
        """
        if (not self.mapping.contains(char)):
            raise Exception("Plug does not exist")

        if self.pairs.contains((char, self.mapping.get(char))):
            self.pairs.remove((char, self.mapping.get(char)))

        if self.pairs.contains((self.mapping.get(char), char)):
            self.pairs.remove((self.mapping.get(char), char))

        self.mapping.remove(self.mapping.get(char))
        self.mapping.remove(char)
        self.size -= 1

    def encrypt(self, plaintext: str) -> str:
        """
            Encrypts a plaintext string using the plugboard.
        """
        ciphertext = ""
        for char in plaintext:
            if self.mapping.contains(char):
                ciphertext += self.mapping.get(char)
            else:
                ciphertext += char
        return ciphertext
