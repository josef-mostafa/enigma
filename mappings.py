from collections import namedtuple
from enum import Enum
from typing import Any, Dict


class Mapping:
    def __init__(self) -> None:
        self.characters: str

    def forward(self, character: Any) -> Any:
        return self.forward_mappings.get(character, character)

    def reverse(self, character: Any) -> Any:
        return self.reverse_mappings.get(character, character)


class CharacterMap(Mapping):
    def __init__(self) -> None:
        self.characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
        self.size = len(self.characters)
        self.forward_mappings: Dict[str, str] = {}
        self.reverse_mappings: Dict[str, str] = {}
        for i, c in enumerate(self.characters):
            self.forward_mappings[c] = str(i + 1)
            self.reverse_mappings[str(i + 1)] = c

    def get_characters(self) -> str:
        return self.characters


class RotorMap(Mapping):
    def __init__(self, mapping_string) -> None:
        self.forward_mappings: Dict[int, int] = {}
        self.reverse_mappings: Dict[int, int] = {}
        chars = CharacterMap()
        for i, c in enumerate(chars.get_characters()):
            self.forward_mappings[int(chars.forward(c))] = int(
                chars.forward(mapping_string[i]))
            self.reverse_mappings[int(chars.forward(mapping_string[i]))] = int(
                chars.forward(c))


class ReflectorMap(Mapping):
    def __init__(self, mapping_string) -> None:
        self.forward_mappings: Dict[int, int] = {}
        self.reverse_mappings: Dict[int, int] = {}
        chars = CharacterMap()
        for i, c in enumerate(chars.get_characters()):
            self.forward_mappings[int(chars.forward(c))] = int(
                chars.forward(mapping_string[i]))

    def reverse(self, character: int) -> int:
        return self.forward.get(character, character)


RotorDefinition = namedtuple("RotorDefinition", ["name", "mapping", "notch"])
ReflectorDefinition = namedtuple("ReflectorDefinition", ["name", "mapping"])


class RotorTypes(Enum):
    I = RotorDefinition(
        "I", "EKMFLGDQVZNTOWYHXUSPAIBRCJekmflgdqvzntowyhxuspaibrcj1234567890", "Q")
    II = RotorDefinition(
        "II", "AJDKSIRUXBLHWTMCQGZNPYFVOEajdksiruxblhwtmcqgznpyfvoe1234567890", "E")
    III = RotorDefinition(
        "III", "BDFHJLCPRTXVZNYEIWGAKMUSQObdfhjlcprtxvznyeiwgakmusqo1234567890", "V")
    IV = RotorDefinition(
        "IV", "ESOVPZJAYQUIRHXLNFTGKDCMWBesovpzjayquirhxlnftgkdcmwb1234567890", "J")
    V = RotorDefinition(
        "V", "VZBRGITYUPSDNHLXAWMJQOFECKvzbrgityupsdnhlxawmjqofeck1234567890", "Z")


class ReflectorTypes(Enum):
    A = ReflectorDefinition(
        "A", "EJMZALYXVBWFCRQUONTSPIKHGDejmzalyxvbwfcrquontspikhgd1234567890")
    B = ReflectorDefinition(
        "B", "YRUHQSLDPXNGOKMIEBFZCWVJATyruhqsldpxngokmiebfzcwvjat1234567890")
    C = ReflectorDefinition(
        "C", "FVPJIAOYEDRZXWGCTKUQSBNMHLfvpjiaoyedrzxwgctkuqsbnmhl1234567890")
