from plugboard import Plugboard
from spindle import Spindle


class Enigma(object):
    def __init__(self) -> None:
        self.spindle: Spindle = Spindle()
        self.plugboard: Plugboard = Plugboard()

    def encrypt(self, plaintext: str) -> str:
        ciphertext = self.plugboard.encrypt(plaintext)
        ciphertext = self.spindle.encrypt(ciphertext)
        ciphertext = self.plugboard.encrypt(ciphertext)
        return ciphertext
