from enum import Enum
from typing import Dict


class Mapping:
    def __init__(self) -> None:
        self.characters: str
        self.forward: Dict[str, str]
        self.reverse: Dict[str, str]

    def forward(self, character: str) -> str:
        return self.forward.get(character, character)

    def reverse(self, character: str) -> str:
        return self.reverse.get(character, character)


class CharacterMap(Mapping):
    def __init__(self) -> None:
        self.characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for i, c in enumerate(self.characters):
            self.forward[c] = str(i)
            self.reverse[str(i)] = c

    def get_characters(self) -> str:
        return self.characters


class RotorMap(Mapping):
    def __init__(self, mapping_string) -> None:
        chars = CharacterMap()
        for i, c in enumerate(chars.get_characters()):
            self.forward[chars.forward(c)] = chars.forward(mapping_string[i])
            self.reverse[chars.forward(mapping_string[i])] = chars.forward(c)


class ReflectorMap(Mapping):
    def __init__(self, mapping_string) -> None:
        chars = CharacterMap()
        for i, c in enumerate(chars.get_characters()):
            self.forward[chars.forward(c)] = chars.forward(mapping_string[i])
    
    def reverse(self, character: str) -> str:
        return self.forward.get(character, character)


class RotorType(Enum):
    I = RotorMap("EKMFLGDQVZNTOWYHXUSPAIBRCJ")
    II = RotorMap("AJDKSIRUXBLHWTMCQGZNPYFVOE")
    III = RotorMap("BDFHJLCPRTXVZNYEIWGAKMUSQO")
    IV = RotorMap("ESOVPZJAYQUIRHXLNFTGKDCMWB")
    V = RotorMap("VZBRGITYUPSDNHLXAWMJQOFECK")


class ReflectorType(Enum):
    B = ReflectorMap("YRUHQSLDPXNGOKMIEBFZCWVJAT")
    C = ReflectorMap("FVPJIAOYEDRZXWGCTKUQSBNMHL")
