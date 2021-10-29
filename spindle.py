from typing import List

from rotor import Rotor


class Spindle(object):
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.rotors: List[Rotor] = []
        self.reflector

    def add_rotor(self, rotor: Rotor) -> None:
        if len(self.rotors) < self.capacity:
            self.rotors.append(rotor)
        else:
            raise Exception("Spindle is full")

    def add_reflector(self, reflector: Rotor) -> None:
        self.reflector = reflector

    def encrypt(self, plaintext: str) -> str:
        ciphertext = ""
        for char in plaintext:
            for index, rotor in enumerate(self.rotors):
                char, notch = rotor.encrypt(char)
                rotor.rotate()
                if notch and index != self.capacity:
                    self.rotors[index+1].rotate
