from plugboard import Plugboard
from spindle import Spindle


class Enigma(object):
    def __init__(self) -> None:
        self.spindle: Spindle
        self.plugboard: Plugboard
