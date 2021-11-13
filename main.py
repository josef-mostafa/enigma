from enigma import Enigma
from mappings import CharacterMap, ReflectorTypes, RotorTypes

e = Enigma()
c = CharacterMap()

menu = {
    1: "Select Rotors",
    2: "Select Reflector",
    3: "Set Rotor Offsets",
    4: "Set Ring Positions",
    5: "Edit Plugboard Connections",
    6: "Set Steps Per Characters",
    7: "Reset Machine",
    8: "Reset Rotors",
    9: "Encrypt",
    0: "Quit"
}


def main():
    while True:
        print("Select an option:")
        for i in menu:
            print(f"{i}: {menu[i]}")
        choice = input("\n> ")
        try:
            choice = int(choice)
            if choice == 1:
                select_rotors()
            elif choice == 2:
                select_reflector()
            elif choice == 3:
                set_rotor_offsets()
            elif choice == 4:
                set_ring_positions()
            elif choice == 5:
                set_plugboard()
            elif choice == 6:
                set_steps_per_character()
            elif choice == 7:
                e.reset()
            elif choice == 8:
                e.spindle.reset_rotors()
            elif choice == 9:
                encrypt()
            elif choice == 0:
                break
            else:
                print("Invalid selection.")
        except ValueError:
            print("Invalid selection.")


def select_rotors():
    print("Current Rotors:")
    for i, r in enumerate(e.spindle.rotors):
        if r is not None:
            print(f"{i+1}: {r.rotor_name}")
        else:
            print(f"{i+1}: --EMPTY--")

    while position := input("\nSelect a rotor to replace: "):
        try:
            position = int(position)
            if position < 1 or position > e.spindle.capacity:
                print("Invalid position.")
                continue
        except ValueError:
                print("Invalid position.")
                continue
        position -= 1
        break

    rotors = enumerate(RotorTypes.__members__.keys())

    for i, name in enumerate(rotors):
        print(f"{i}: {name}")

    while rotor := input("\nSelect a rotor: "):
        try:
            rotor = int(rotor)
            if rotor < 1 or rotor > len(RotorTypes):
                print("Invalid rotor.")
                continue
        except ValueError:
                print("Invalid rotor.")
                continue
        position -= 1
        break

    e.spindle.set_rotor(RotorTypes.__members__[rotors[rotor]].value, position)



def select_reflector():
    if e.spindle.reflector is not None:
        print(f"Current Reflector: {e.spindle.reflector.reflector_name}")
    else:
        print("Current Reflector: --EMPTY--")

    reflectors = enumerate(ReflectorTypes.__members__.keys())

    for i, name in enumerate(reflectors):
        print(f"{i}: {name}")

    while reflector := input("\nSelect a reflector: "):
        try:
            reflector = int(reflector)
            if reflector < 1 or reflector > len(ReflectorTypes):
                print("Invalid reflector.")
                continue
        except ValueError:
                print("Invalid reflector.")
                continue
        break

    e.spindle.set_reflector(ReflectorTypes.__members__[reflectors[reflector]].value)



def set_rotor_offsets():
    print("Current Rotor Offsets:")
    for i, r in enumerate(e.spindle.rotors):
        if r is not None:
            print(f"{i+1}: {r.rotor_name}, offset: {r.rotor_offset}")
        else:
            print(f"{i+1}: --EMPTY--")

    while position := input("\nSelect a rotor to change its offset: "):
        try:
            position = int(position)
            if position < 1 or position > e.spindle.capacity:
                print("Invalid position.")
                continue
        except ValueError:
                print("Invalid position.")
                continue
        position -= 1
        break

    while offset := input("\nEnter the new offset: "):
        try:
            offset = int(offset)
            if offset < 1 or offset > c.size:
                print("Invalid offset.")
                continue
        except ValueError:
            print("Invalid offset.")
            continue
        break

    e.spindle.set_rotor_offset(position, offset)


def set_ring_positions():
    print("Current Ring Positions:")
    for i, r in enumerate(e.spindle.rotors):
        if r is not None:
            print(f"{i+1}: {r.rotor_name}, ring position: {r.ring_position}")
        else:
            print(f"{i+1}: --EMPTY--")

    while position := input("\nSelect a rotor to change its ring position: "):
        try:
            position = int(position)
            if position < 1 or position > e.spindle.capacity:
                print("Invalid position.")
                continue
        except ValueError:
                print("Invalid position.")
                continue
        position -= 1
        break

    while ring_position := input("\nEnter the new ring position: "):
        try:
            ring_position = int(ring_position)
            if ring_position < 1 or ring_position > c.size:
                print("Invalid ring position.")
                continue
        except ValueError:
            print("Invalid ring position.")
            continue
        break

    e.spindle.set_ring_position(position, ring_position)


def set_steps_per_character():
    pass


def set_plugboard():
    pass


def encrypt():
    pass


if __name__ == "__main__":
    main()
