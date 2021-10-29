from typing import Set

from mappings import ReflectorMap, RotorMap, RotorType, ReflectorType


class Rotor(object):
    def __init__(self, rotor_type: RotorType) -> None:
        self.rotor_type = rotor_type
        self.notches: Set[int]
        self.rotor_map: RotorMap
        self.ring_position: int
        self.rotor_offset: int
        self.rotor_size: int
        self.reset()

    def reset(self) -> None:
        self.rotor_offset = 1
        self.ring_position = 0
        self.notches = set()
        self.rotor_map = RotorMap(self.rotor_type)
        self.rotor_size = 26

    def set_position(self, position: int) -> None:
        if position <= 0 or position > self.rotor_size:
            raise ValueError("Invalid position")
        self.ring_position = position

    def add_notch(self, notch: int) -> None:
        if notch <= 0 or notch > self.rotor_size:
            raise ValueError("Invalid notch position")
        self.notches.add(notch)

    def rotate(self) -> bool:
        """
            Advances the rotor position by one.
            Returns True if the rotor has passed one of its notches.
        """
        passed_notch = self.rotor_offset in self.notches
        if self.rotor_offset == self.rotor_size:
            self.rotor_offset = 1
        self.rotor_offset += 1
        return passed_notch

    def forward(self, char: int) -> int:
        if char <= 0 or char > self.rotor_size:
            raise ValueError("Invalid character")
        return self.rotor_map[char]

    def reverse(self, char: int) -> int:
        if char <= 0 or char > self.rotor_size:
            raise ValueError("Invalid character")
        return self.rotor_map[char]


class Reflector(object):
    def __init__(self, reflector_type: ReflectorType) -> None:
        self.reflector_type = reflector_type
        self.reflector_map: ReflectorMap
        self.reset()

    def reset(self) -> None:
        self.reflector_map = RotorMap(self.reflector_type)

    def forward(self, char: int) -> int:
        if char <= 0 or char > self.rotor_size:
            raise ValueError("Invalid character")
        return self.rotor_map[char]
