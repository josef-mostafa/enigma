from typing import List

from mappings import CharacterMap, ReflectorDefinition, RotorDefinition
from rotor import Reflector, Rotor


class Spindle(object):
    def __init__(self, capacity: int = 3) -> None:
        self.capacity = capacity
        self.rotors: List[Rotor] = [None] * capacity
        self.ring_positions: List[int] = [1] * capacity
        self.rotor_offsets: List[int] = [1] * capacity
        self.reflector: Reflector = None
        self.chars_map: CharacterMap = CharacterMap()
        self.steps_per_character: int = 1

    def __repr__(self) -> str:
        return "Rotors:\n" + "\n".join(map(lambda r: f"{r[0]}: {r[1].__repr__()}", enumerate(self.rotors, 1))) + "\nReflector: " + self.reflector.__repr__() + "\nSteps Per Character: " + self.steps_per_character

    def set_capacity(self, capacity: int) -> None:
        if capacity < 1:
            raise ValueError("Capacity must be at least 1")
        self.capacity = capacity

    def set_steps_per_character(self, steps_per_character: int) -> None:
        if steps_per_character < 1:
            raise ValueError("Steps per character must be at least 1")
        self.steps_per_character = steps_per_character

    def set_rotor(self, rotor: RotorDefinition, position: int) -> None:
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

    def set_reflector(self, reflector: ReflectorDefinition) -> None:
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
        # for char in map(lambda x: int(self.chars_map.forward(x)), plaintext):
        for character in plaintext:
            char = int(self.chars_map.forward(character))

            # rotate the rotors
            for i in range(self.steps_per_character):
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
