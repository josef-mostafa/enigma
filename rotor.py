from typing import Set

from mappings import CharacterMap, ReflectorMap, ReflectorType, RotorMap, RotorType


class Rotor(object):
    def __init__(self, rotor_type: RotorType) -> None:
        self.rotor_type = rotor_type
        self.rotor_map: RotorMap
        self.chars: Set[int]
        self.chars_map: CharacterMap
        self.rotor_size: int
        self.notches: Set[int]
        self.ring_position: int
        self.rotor_offset: int
        self.reset()

    def __repr__(self) -> str:
        return f"{RotorType}: {self.rotor_offset}"

    def reset(self) -> None:
        self.rotor_map = RotorMap(self.rotor_type.value.mapping)
        self.chars_map = CharacterMap()
        self.rotor_size = self.chars_map.size
        self.chars = set(range(1, self.rotor_size + 1))
        self.rotor_offset = 1
        self.ring_position = 1
        self.notches = {int(self.chars_map.forward(self.rotor_type.value.notch))}

    def set_ring_position(self, position: int) -> None:
        if position not in self.chars:
            raise ValueError("Invalid position")
        self.ring_position = position

    def set_rotor_offset(self, offset: int) -> None:
        if offset not in self.chars:
            raise ValueError("Invalid offset")
        self.rotor_offset = offset

    def add_notch(self, notch: int) -> None:
        if notch not in self.chars:
            raise ValueError("Invalid notch position")
        self.notches.add(notch)

    def remove_notch(self, notch: int) -> None:
        if notch not in self.chars:
            raise ValueError("Invalid notch position")
        self.notches.remove(notch)

    def rotate(self) -> bool:
        """
            Returns True if the rotor has passed one of its notches.
        """
        passed_notch = self.rotor_offset in self.notches
        if self.rotor_offset == self.rotor_size:
            self.rotor_offset = 0
        self.rotor_offset += 1
        while self.rotor_offset > 26:
            self.rotor_offset -= 26
        return passed_notch

    def forward(self, char: int) -> int:
        if char not in self.chars:
            raise ValueError("Invalid character")
        char += self.rotor_offset - self.ring_position
        while char > 26:
            char -= 26
        while char < 1:
            char += 26
        char = self.rotor_map.forward(char)
        char -= self.rotor_offset - self.ring_position
        while char > 26:
            char -= 26
        while char < 1:
            char += 26
        return char

    def reverse(self, char: int) -> int:
        if char not in self.chars:
            raise ValueError("Invalid character")
        char += self.rotor_offset - self.ring_position
        while char > 26:
            char -= 26
        while char < 1:
            char += 26
        char = self.rotor_map.reverse(char)
        char -= self.rotor_offset - self.ring_position
        while char > 26:
            char -= 26
        while char < 1:
            char += 26
        return char


class Reflector(object):
    def __init__(self, reflector_type: ReflectorType) -> None:
        self.reflector_type = reflector_type
        self.reflector_map: ReflectorMap
        self.chars: Set[int]
        self.reflector_size: int
        self.reset()

    def reset(self) -> None:
        self.reflector_map = ReflectorMap(self.reflector_type.value)
        self.chars_map = CharacterMap()
        self.reflector_size = self.chars_map.size
        self.chars = set(range(1, self.reflector_size + 1))

    def forward(self, char: int) -> int:
        if char not in self.chars:
            raise ValueError("Invalid character")
        return self.reflector_map.forward(char)
