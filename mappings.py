from collections import namedtuple
from enum import Enum
from typing import Dict


class Mapping:
    def __init__(self) -> None:
        self.characters: str

    def forward(self, character: str) -> str:
        return self.forward_mappings.get(character, character)

    def reverse(self, character: str) -> str:
        return self.reverse_mappings.get(character, character)


class CharacterMap(Mapping):
    def __init__(self) -> None:
        self.characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.forward_mappings: Dict[str, str] = {}
        self.reverse_mappings: Dict[str, str] = {}
        for i, c in enumerate(self.characters):
            self.forward_mappings[c] = str(i + 1)
            self.reverse_mappings[str(i + 1)] = c

    def get_characters(self) -> str:
        return self.characters


class RotorMap(Mapping):
    def __init__(self, mapping_string) -> None:
        self.forward_mappings: Dict[str, str] = {}
        self.reverse_mappings: Dict[str, str] = {}
        chars = CharacterMap()
        for i, c in enumerate(chars.get_characters()):
            self.forward_mappings[chars.forward(c)] = chars.forward(mapping_string[i])
            self.reverse_mappings[chars.forward(mapping_string[i])] = chars.forward(c)


class ReflectorMap(Mapping):
    def __init__(self, mapping_string) -> None:
        self.forward_mappings: Dict[str, str] = {}
        self.reverse_mappings: Dict[str, str] = {}
        chars = CharacterMap()
        for i, c in enumerate(chars.get_characters()):
            self.forward_mappings[chars.forward(c)] = chars.forward(mapping_string[i])

    def reverse(self, character: str) -> str:
        return self.forward.get(character, character)


RotorDefinition = namedtuple("RotorDefinition", ["mapping", "notch"])


class RotorType(Enum):
    I = RotorDefinition("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q")
    II = RotorDefinition("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E")
    III = RotorDefinition("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V")
    IV = RotorDefinition("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J")
    V = RotorDefinition("VZBRGITYUPSDNHLXAWMJQOFECK", "Z")


class ReflectorType(Enum):
    A = "EJMZALYXVBWFCRQUONTSPIKHGD"
    B = "YRUHQSLDPXNGOKMIEBFZCWVJAT"
    C = "FVPJIAOYEDRZXWGCTKUQSBNMHL"
