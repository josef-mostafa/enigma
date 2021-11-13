from typing import Set

from mappings import (CharacterMap, ReflectorDefinition, ReflectorMap,
                      RotorDefinition, RotorMap)


class Rotor(object):
    def __init__(self, rotor_definition: RotorDefinition) -> None:
        self.rotor_definition = rotor_definition
        self.rotor_name: str = self.rotor_definition.name
        self.rotor_map: RotorMap = RotorMap(self.rotor_definition.mapping)
        self.chars_map: CharacterMap = CharacterMap()
        self.rotor_size: int = self.chars_map.size
        self.chars: Set[int] = set(range(1, self.rotor_size + 1))
        self.notches: Set[int] = {
            int(self.chars_map.forward(self.rotor_definition.notch))}
        self.rotor_offset: int = 1
        self.ring_position: int = 1

    def __repr__(self) -> str:
        return f"{self.rotor_name} - Rotor Offset: {self.rotor_offset} - Ring Position: {self.ring_position}"

    def reset(self) -> None:
        """
            Resets the rotor to its initial position.
        """
        self.rotor_offset = 1
        self.ring_position = 1

    def set_ring_position(self, position: int) -> None:
        """
            Sets the ring position of the rotor.
        """
        if position not in self.chars:
            raise ValueError("Invalid position")
        self.ring_position = position

    def set_rotor_offset(self, offset: int) -> None:
        """
            Sets the rotor offset.
        """
        if offset not in self.chars:
            raise ValueError("Invalid offset")
        self.rotor_offset = offset

    def rotate(self) -> bool:
        """
            Advances the rotor by one step.
            Returns True if the rotor has passed one of its notches.
        """
        passed_notch = self.rotor_offset in self.notches
        if self.rotor_offset == self.rotor_size:
            self.rotor_offset = 0
        self.rotor_offset += 1
        while self.rotor_offset > self.chars_map.size:
            self.rotor_offset -= self.chars_map.size
        return passed_notch

    def update_char(self, char: int) -> int:
        """
            Updates the character to be within the range of the rotor.
        """
        while char > self.chars_map.size:
            char -= self.chars_map.size
        while char < 1:
            char += self.chars_map.size
        return char

    def forward(self, char: int) -> int:
        """
            Moves the character forwards through the rotor.
        """
        if char not in self.chars:
            raise ValueError("Invalid character")
        char = self.update_char(
            char + (self.rotor_offset - self.ring_position))
        char = self.rotor_map.forward(char)
        char = self.update_char(
            char - (self.rotor_offset - self.ring_position))
        return char

    def reverse(self, char: int) -> int:
        """
            Moves the character backwards through the rotor.
        """
        if char not in self.chars:
            raise ValueError("Invalid character")
        char = self.update_char(
            char + (self.rotor_offset - self.ring_position))
        char = self.rotor_map.reverse(char)
        char = self.update_char(
            char - (self.rotor_offset - self.ring_position))
        return char


class Reflector(object):
    def __init__(self, reflector_definition: ReflectorDefinition) -> None:
        self.reflector_definiton = reflector_definition
        self.reflector_name: str = self.reflector_definiton.name
        self.reflector_map: ReflectorMap = ReflectorMap(
            self.reflector_definiton.mapping)
        self.chars_map: CharacterMap = CharacterMap()
        self.reflector_size: int = self.chars_map.size
        self.chars: Set[int] = set(range(1, self.reflector_size + 1))

    def __repr__(self) -> str:
        return self.reflector_name

    def forward(self, char: int) -> int:
        """
            Moves the character through the reflector.
        """
        if char not in self.chars:
            raise ValueError("Invalid character")
        return self.reflector_map.forward(char)
