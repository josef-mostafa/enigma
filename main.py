from mappings import ReflectorType, RotorType
from spindle import Spindle


def main():
    s = Spindle(3)
    s.set_rotor(RotorType.I, 0)
    s.set_rotor(RotorType.II, 1)
    s.set_rotor(RotorType.III, 2)
    s.set_reflector(ReflectorType.A)
    s.set_ring_position(0, 2)
    s.set_ring_position(1, 6)
    s.set_ring_position(2, 10)
    print(s.encrypt("MAZENAMRAHMED"))


if __name__ == "__main__":
    main()
