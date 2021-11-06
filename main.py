from enigma import Enigma
from mappings import ReflectorType, RotorType


def main():
    e = Enigma()
    e.spindle.set_rotor(RotorType.III, 0)
    e.spindle.set_rotor(RotorType.II, 1)
    e.spindle.set_rotor(RotorType.I, 2)
    e.spindle.set_reflector(ReflectorType.A)
    e.spindle.set_ring_position(0, 2)
    e.spindle.set_ring_position(1, 6)
    e.spindle.set_ring_position(2, 10)
    e.plugboard.add_plug("A", "K")
    e.plugboard.add_plug("R", "P")
    e.plugboard.add_plug("S", "J")
    e.plugboard.add_plug("D", "N")
    e.plugboard.add_plug("F", "X")
    e.plugboard.add_plug("G", "U")
    e.plugboard.add_plug("L", "B")
    e.plugboard.add_plug("I", "Y")
    e.spindle.set_double_step(True)
    s = e.encrypt("TESTTESTHELLOWORLDTESTHELLOWORLDTESTTESTHELLOWORLDHELLOWORLDTESTHELLOWORLD")
    print(s)
    e.spindle.reset_rotors()
    e.spindle.set_ring_position(0, 2)
    e.spindle.set_ring_position(1, 6)
    e.spindle.set_ring_position(2, 10)
    print(e.encrypt(s))


if __name__ == "__main__":
    main()
