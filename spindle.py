from datastructs import Array
from mappings import CharacterMap, ReflectorDefinition, RotorDefinition
from rotor import Reflector, Rotor


class Spindle(object):
    def __init__(self, capacity: int = 3) -> None:
        self.capacity = capacity
        self.rotors: Array = Array(self.capacity)
        self.ring_positions: Array = Array(self.capacity, 1)
        self.rotor_offsets: Array = Array(self.capacity, 1)
        self.reflector: Reflector = None
        self.chars_map: CharacterMap = CharacterMap()
        self.steps_per_character: int = 1

    def __repr__(self) -> str:
        s = "Rotors:\n"
        for i in range(self.capacity):
            s += f"{i+1}: {self.rotors.get(i)}\n"
        s += "Reflector: " + self.reflector.__repr__()
        s += f"\nSteps Per Character: {self.steps_per_character}"
        return s

    def set_capacity(self, capacity: int) -> None:
        """
            Sets the capacity of the spindle (how many rotors it can take).
        """
        if capacity < 1:
            raise ValueError("Capacity must be at least 1")
        self.capacity = capacity

    def set_steps_per_character(self, steps_per_character: int) -> None:
        """
            Sets the number of steps (rotations) to apply to the first rotor per character.
        """
        if steps_per_character < 1:
            raise ValueError("Steps per character must be at least 1")
        self.steps_per_character = steps_per_character

    def set_rotor(self, rotor: RotorDefinition, position: int) -> None:
        """
            Sets the rotor at the given position.
        """
        if position < 0 or position >= self.capacity:
            raise ValueError("Invalid position")
        r = Rotor(rotor)
        r.set_ring_position(self.ring_positions.get(position))
        r.set_rotor_offset(self.rotor_offsets.get(position))
        self.rotors.set_item(position, r)

    def set_ring_position(self, position: int, ring_position: int) -> None:
        """
            Sets the ring position of the rotor at the given position.
        """
        if position < 0 or position >= self.capacity:
            raise ValueError("Invalid position")
        self.ring_positions.set_item(position, ring_position)
        if self.rotors.get(position) is not None:
            r = self.rotors.get(position)
            r.set_ring_position(self.ring_positions.get(position))

    def set_rotor_offset(self, position: int, rotor_offset: int) -> None:
        """
            Sets the rotor offset of the rotor at the given position.
        """
        if position < 0 or position >= self.capacity:
            raise ValueError("Invalid position")
        self.rotor_offsets.set_item(position, rotor_offset)
        if self.rotors.get(position) is not None:
            r = self.rotors.get(position)
            r.set_rotor_offset(self.rotor_offsets.get(position))

    def set_reflector(self, reflector: ReflectorDefinition) -> None:
        """
            Sets the reflector.
        """
        self.reflector = Reflector(reflector)

    def reset_rotors(self) -> None:
        """
            Resets the rotors to their initial positions.
        """
        for i in range(self.capacity):
            rotor = self.rotors.get(i)
            if rotor is not None:
                rotor.reset()
        self.ring_positions = Array(self.capacity, 1)
        self.rotor_offsets = Array(self.capacity, 1)

    def step_rotors(self) -> None:
        """
            Steps the rotors.
        """
        for i in range(self.capacity):
            r = self.rotors.get(i)
            if (r.rotate()):
                i += 1
                continue
            break
        for i in range(self.capacity):
            self.rotor_offsets.set_item(i, self.rotors.get(i).rotor_offset)

    def encrypt(self, plaintext: str) -> str:
        """
            Encrypts the given plaintext.
        """
        for i in range(self.capacity):
            r = self.rotors.get(i)
            if r is None:
                raise Exception("One of the rotors is missing")
        if self.reflector is None:
            raise Exception("The reflector is missing")

        ciphertext = ""
        for character in plaintext:
            char = int(self.chars_map.forward(character))

            # rotate the rotors
            for i in range(self.steps_per_character):
                self.step_rotors()

            # encrypt through the rotors forwards
            for i in range(self.capacity):
                rotor = self.rotors.get(i)
                char = rotor.forward(char)

            # reflect through the reflector
            char = self.reflector.forward(char)

            # encrypt through the rotors backwards
            for i in reversed(range(self.capacity)):
                rotor = self.rotors.get(i)
                char = rotor.reverse(char)

            ciphertext += self.chars_map.reverse(str(char))

        return ciphertext
