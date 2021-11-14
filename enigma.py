from plugboard import Plugboard
from spindle import Spindle


class Enigma(object):
    def __init__(self) -> None:
        self.spindle: Spindle = Spindle()
        self.plugboard: Plugboard = Plugboard()

    def __repr__(self) -> None:
        return f"Spindle:\n{self.spindle}\n\nPlugboard:\n{self.plugboard}"

    def reset(self) -> None:
        """
            Resets the spindle and plugboard.
        """
        self.spindle = Spindle()
        self.plugboard = Plugboard()

    def encrypt(self, plaintext: str) -> str:
        """
            Encrypts the plaintext using the spindle and plugboard.
        """
        ciphertext = self.plugboard.encrypt(plaintext)
        ciphertext = self.spindle.encrypt(ciphertext)
        ciphertext = self.plugboard.encrypt(ciphertext)
        return ciphertext
