from collections import namedtuple
from enum import Enum
from typing import Any

from datastructs import Map


class Mapping:
    def __init__(self) -> None:
        self.characters: str

    def forward(self, character: Any) -> Any:
        return self.forward_mappings.get(character)

    def reverse(self, character: Any) -> Any:
        return self.reverse_mappings.get(character)


class CharacterMap(Mapping):
    """
        This class is used to map characters to their number equivalent and vice versa.
    """
    def __init__(self) -> None:
        self.characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
        self.size = len(self.characters)
        self.forward_mappings: Map = Map(self.size)
        self.reverse_mappings: Map = Map(self.size)
        for i, c in enumerate(self.characters):
            self.forward_mappings.insert(c, str(i + 1))
            self.reverse_mappings.insert(str(i + 1), c)

    def get_characters(self) -> str:
        return self.characters


class RotorMap(Mapping):
    """
        This class is used to represent a rotor mapping.
    """
    def __init__(self, mapping_string) -> None:
        chars = CharacterMap()
        self.forward_mappings: Map = Map(chars.size)
        self.reverse_mappings: Map = Map(chars.size)
        for i, c in enumerate(chars.get_characters()):
            self.forward_mappings.insert(int(chars.forward(c)), int(
                chars.forward(mapping_string[i])))
            self.reverse_mappings.insert(int(chars.forward(mapping_string[i])), int(
                chars.forward(c)))


class ReflectorMap(Mapping):
    """
        This class is used to represent a reflector mapping.
    """
    def __init__(self, mapping_string) -> None:
        chars = CharacterMap()
        self.forward_mappings: Map = Map(chars.size)
        for i, c in enumerate(chars.get_characters()):
            self.forward_mappings.insert(int(chars.forward(c)), int(
                chars.forward(mapping_string[i])))

    def reverse(self, character: int) -> int:
        return self.forward.get(character, character)


RotorDefinition = namedtuple("RotorDefinition", ["name", "mapping", "notch"])
ReflectorDefinition = namedtuple("ReflectorDefinition", ["name", "mapping"])


class RotorTypes(Enum):
    """
        These are the default rotors used in the Enigma machine.
    """
    I = RotorDefinition(
        "I", "DjcBiLkns1IMzoVOa8lWx7tu0wGfvYpTdrC65mh9UFyZgXqAEbK2JPNQRS43eH", "Q")
    II = RotorDefinition(
        "II", "X90qOErIuWLCM6ZhvwYslzAt2nkbapfFeN4SJ1T7jV3HKi5DRPmUd8QcyogxBG", "E")
    III = RotorDefinition(
        "III", "x81pMnmrUz3vew6qQlyObR752TASiXGKZLCkd0DoafBcNhYtV9ujJEgsHFI4PW", "V")
    IV = RotorDefinition(
        "IV", "uTdmON85Hr0oMRvSpcwsLUjh3FJCGKXQ6BYt2exVfz4qZAEWiyD7kbaPg1lI9n", "J")
    V = RotorDefinition(
        "V", "b8md0Ci5jZyYpSkhwJoAnzFPeLxsX1qMWKDHTEV2c43gR9a6Uv7ItlrfQuNOGB", "Z")


class ReflectorTypes(Enum):
    """
        These are the default reflectors used in the Enigma machine.
    """
    A = ReflectorDefinition(
        "A", "EJMZALYXVBWFCRQUONTSPIKHGDejmzalyxvbwfcrquontspikhgd1234567890")
    B = ReflectorDefinition(
        "B", "YRUHQSLDPXNGOKMIEBFZCWVJATyruhqsldpxngokmiebfzcwvjat1234567890")
    C = ReflectorDefinition(
        "C", "FVPJIAOYEDRZXWGCTKUQSBNMHLfvpjiaoyedrzxwgctkuqsbnmhl1234567890")
