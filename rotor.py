from typing import List, Set

from mappings import ReflectorMap, ReflectorType, RotorMap, RotorType


class Rotor(object):
    def __init__(self, rotor_type: RotorType) -> None:
        self.rotor_type = rotor_type
        self.notches: Set[int]
        self.rotor_map: RotorMap
        self.ring_position: int
        self.rotor_offset: int
        self.rotor_size: int
        self.chars: List[str]
        self.reset()

    def __repr__(self) -> str:
        return f"{RotorType}: {self.rotor_offset}"

    def reset(self) -> None:
        self.rotor_offset = 1
        self.ring_position = 0
        self.notches = set(self.rotor_type.value.notch)
        self.rotor_map = RotorMap(self.rotor_type.value.mapping)
        self.rotor_size = 26
        self.chars = set(map(str, range(1, self.rotor_size + 1)))

    def set_ring_position(self, position: int) -> None:
        if position < 0 or position > self.rotor_size:
            raise ValueError("Invalid position")
        self.ring_position = position

    def set_rotor_offset(self, offset: int) -> None:
        if offset <= 0 or offset > self.rotor_size:
            raise ValueError("Invalid offset")
        self.rotor_offset = offset

    def add_notch(self, notch: int) -> None:
        if notch <= 0 or notch > self.rotor_size:
            raise ValueError("Invalid notch position")
        self.notches.add(notch)

    def remove_notch(self, notch: int) -> None:
        if notch <= 0 or notch > self.rotor_size:
            raise ValueError("Invalid notch position")
        self.notches.remove(notch)

    def rotate(self) -> bool:
        """
            Returns True if the rotor has passed one of its notches.
        """
        passed_notch = self.rotor_offset in self.notches
        if self.rotor_offset == self.rotor_size:
            self.rotor_offset = 1
        self.rotor_offset += 1
        return passed_notch

    def forward(self, char: str) -> str:
        if char not in self.chars:
            raise ValueError("Invalid character")
        return self.rotor_map.forward(char)

    def reverse(self, char: str) -> str:
        if char not in self.chars:
            raise ValueError("Invalid character")
        return self.rotor_map.reverse(char)


class Reflector(object):
    def __init__(self, reflector_type: ReflectorType) -> None:
        self.reflector_type = reflector_type
        self.reflector_map: ReflectorMap
        self.reflector_size: int
        self.chars: List[str]
        self.reset()

    def reset(self) -> None:
        self.reflector_map = ReflectorMap(self.reflector_type.value)
        self.reflector_size = 26
        self.chars = set(map(str, range(1, self.reflector_size + 1)))

    def forward(self, char: str) -> str:
        if char not in self.chars:
            raise ValueError("Invalid character")
        return self.reflector_map.forward(char)
