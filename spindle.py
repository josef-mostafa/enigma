from typing import List

from mappings import CharacterMap, ReflectorType, RotorType
from rotor import Reflector, Rotor


class Spindle(object):
    def __init__(self, capacity: int = 3) -> None:
        self.capacity = capacity
        self.rotors: List[Rotor] = [None] * capacity
        self.ring_positions: List[int] = [1] * capacity
        self.rotor_offsets: List[int] = [1] * capacity
        self.reflector: Reflector
        self.chars_map: CharacterMap = CharacterMap()
        self.double_step: bool = False

    def set_double_step(self, double_step: bool) -> None:
        self.double_step = double_step

    def set_capacity(self, capacity: int) -> None:
        self.capacity = capacity

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

    def reset_rotors(self) -> None:
        for rotor in self.rotors:
            rotor.reset()
        self.ring_positions = [1] * self.capacity
        self.rotor_offsets = [1] * self.capacity

    def step_rotors(self) -> None:
        for i in range(self.capacity):
            if (self.rotors[i].rotate()):
                i += 1
                continue
            break
        self.rotor_offsets = [r.rotor_offset for r in self.rotors]


    def encrypt(self, plaintext: str) -> str:
        if any([r == None for r in self.rotors + [self.reflector]]):
            raise Exception("One of the rotors or the reflector is missing")

        ciphertext = ""
        for char in map(lambda x: int(self.chars_map.forward(x)), plaintext):
            # rotate the rotors
            self.step_rotors()

            # double step
            if self.double_step:
                self.step_rotors()

            # encrypt through the rotors forwards
            for rotor in self.rotors:
                char = rotor.forward(char)

            # reflect through the reflector
            char = self.reflector.forward(char)

            # encrypt through the rotors backwards
            for rotor in reversed(self.rotors):
                char = rotor.reverse(char)

            ciphertext += self.chars_map.reverse(str(char))

        return ciphertext
