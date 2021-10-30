from typing import List

from mappings import CharacterMap, ReflectorType, RotorType
from rotor import Reflector, Rotor


class Spindle(object):
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.rotors: List[Rotor] = [None] * capacity
        self.ring_positions: List[int] = [0] * capacity
        self.rotor_offsets: List[int] = [1] * capacity
        self.reflector: Reflector
        self.chars: CharacterMap = CharacterMap()

    def set_rotor(self, rotor: RotorType, position: int) -> None:
        if position < 0 or position >= self.capacity:
            raise ValueError("Invalid position")
        self.rotors[position] = Rotor(rotor)
        self.rotors[position].set_ring_position(self.ring_positions[position])
        self.rotors[position].set_rotor_offset(self.rotor_offsets[position])

    def set_ring_position(self, position: int, ring_position: int) -> None:
        if position < 0 or position >= self.capacity:
            raise ValueError("Invalid position")
        self.ring_positions[position] = ring_position
        self.rotors[position].set_ring_position(self.ring_positions[position])

    def set_rotor_offset(self, position: int, rotor_offset: int) -> None:
        if position < 0 or position >= self.capacity:
            raise ValueError("Invalid position")
        self.rotor_offsets[position] = rotor_offset
        self.rotors[position].set_rotor_offset(self.rotor_offsets[position])

    def set_reflector(self, reflector: ReflectorType) -> None:
        self.reflector = Reflector(reflector)

    def encrypt(self, plaintext: str) -> str:
        ciphertext = ""
        for char in map(lambda x: self.chars.forward(x), plaintext):
            while (i := 0 < self.capacity):
                if (self.rotors[i].rotate()):
                    i += 1
                else:
                    break

            for rotor in self.rotors:
                char = rotor.forward(char)

            char = self.reflector.forward(char)

            for rotor in reversed(self.rotors):
                char = rotor.reverse(char)

            ciphertext += self.chars.reverse(char)
