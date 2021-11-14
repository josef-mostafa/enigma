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
    """
        These are the default reflectors used in the Enigma machine.
    """
    A = ReflectorDefinition(
        "A", "EJMZALYXVBWFCRQUONTSPIKHGDejmzalyxvbwfcrquontspikhgd1234567890")
    B = ReflectorDefinition(
        "B", "YRUHQSLDPXNGOKMIEBFZCWVJATyruhqsldpxngokmiebfzcwvjat1234567890")
    C = ReflectorDefinition(
        "C", "FVPJIAOYEDRZXWGCTKUQSBNMHLfvpjiaoyedrzxwgctkuqsbnmhl1234567890")
