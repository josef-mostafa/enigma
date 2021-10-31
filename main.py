from mappings import ReflectorType, RotorType
from spindle import Spindle


def main():
    s = Spindle(3)
    s.set_rotor(RotorType.I, 0)
    s.set_rotor(RotorType.II, 1)
    s.set_rotor(RotorType.III, 2)
    s.set_reflector(ReflectorType.A)
    print(s.encrypt("ENIGMATEST"))


if __name__ == "__main__":
    main()
