import os

from enigma import Enigma
from mappings import CharacterMap, ReflectorTypes, RotorTypes

enigma = Enigma()
c = CharacterMap()

menu = {
    1: "Select Rotors",
    2: "Select Reflector",
    3: "Set Rotor Offsets",
    4: "Set Ring Positions",
    5: "Set Steps Per Characters",
    6: "Add Plugboard Connection",
    7: "Remove Plugboard Connection",
    8: "Reset Machine",
    9: "Reset Rotors",
    10: "Reset Plugboard",
    11: "Encrypt",
    12: "Print Current Configuration",
    0: "Quit"
}


def main():
    while True:
        if os.name == "posix":
            _ = os.system("clear")
        else:
            _ = os.system("cls")

        print("Main Menu:")
        for i in menu:
            print(f"{i}: {menu[i]}")
        choice = input("\nSelect an option: ")
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
                set_steps_per_character()
            elif choice == 6:
                add_plugboard_connection()
            elif choice == 7:
                remove_plugboard_connection()
            elif choice == 8:
                enigma.reset()
            elif choice == 9:
                enigma.spindle.reset_rotors()
            elif choice == 10:
                enigma.plugboard.reset()
            elif choice == 11:
                encrypt()
            elif choice == 12:
                print(enigma)
            elif choice == 0:
                break
            else:
                print("Invalid selection.")
        except ValueError:
            print("Invalid selection.")
        input("Press any key to continue...")


def select_rotors():
    print("Current Rotors:")
    for i in range(1, enigma.spindle.capacity + 1):
        print(f"{i}: {enigma.spindle.rotors.get(i - 1)}")

    while (position := input("\nSelect a rotor to replace: ")) or True:
        try:
            position = int(position)
            if position < 1 or position > enigma.spindle.capacity:
                print("Invalid position.")
                continue
        except ValueError:
            print("Invalid position.")
            continue
        position -= 1
        break

    rotors = dict(enumerate(RotorTypes.__members__.keys(), 1))

    for i, name in rotors.items():
        print(f"{i}: {name}")

    while (rotor := input("\nSelect a rotor: ")) or True:
        try:
            rotor = int(rotor)
            if rotor < 1 or rotor > len(RotorTypes):
                print("Invalid rotor.")
                continue
        except ValueError:
            print("Invalid rotor.")
            continue
        break

    enigma.spindle.set_rotor(RotorTypes.__members__[
                             rotors[rotor]].value, position)


def select_reflector():
    print(f"Current Reflector: {enigma.spindle.reflector}")

    reflectors = dict(enumerate(ReflectorTypes.__members__.keys(), 1))

    for i, name in reflectors.items():
        print(f"{i}: {name}")

    while (reflector := input("\nSelect a reflector: ")) or True:
        try:
            reflector = int(reflector)
            if reflector < 1 or reflector > len(ReflectorTypes):
                print("Invalid reflector.")
                continue
        except ValueError:
            print("Invalid reflector.")
            continue
        break

    enigma.spindle.set_reflector(ReflectorTypes.__members__[
        reflectors[reflector]].value)


def set_rotor_offsets():
    print("Current Rotor Offsets:")
    for i in range(enigma.spindle.capacity):
        print(f"{i}: offset: {enigma.spindle.rotor_offsets.get(i)}")

    while (position := input("\nSelect a rotor to change its offset: ")) or True:
        try:
            position = int(position)
            if position < 1 or position > enigma.spindle.capacity:
                print("Invalid position.")
                continue
        except ValueError:
            print("Invalid position.")
            continue
        position -= 1
        break

    while (offset := input("\nEnter the new offset: ")) or True:
        try:
            offset = int(offset)
            if offset < 1 or offset > c.size:
                print("Invalid offset.")
                continue
        except ValueError:
            print("Invalid offset.")
            continue
        break

    enigma.spindle.set_rotor_offset(position, offset)


def set_ring_positions():
    print("Current Ring Positions:")
    for i in range(enigma.spindle.capacity):
        print(f"{i}: offset: {enigma.spindle.ring_positions.get(i)}")

    while (position := input("\nSelect a rotor to change its ring position: ")) or True:
        try:
            position = int(position)
            if position < 1 or position > enigma.spindle.capacity:
                print("Invalid position.")
                continue
        except ValueError:
            print("Invalid position.")
            continue
        position -= 1
        break

    while (ring_position := input("\nEnter the new ring position: ")) or True:
        try:
            ring_position = int(ring_position)
            if ring_position < 1 or ring_position > c.size:
                print("Invalid ring position.")
                continue
        except ValueError:
            print("Invalid ring position.")
            continue
        break

    enigma.spindle.set_ring_position(position, ring_position)


def set_steps_per_character():
    print(f"Current Steps Per Character: {enigma.spindle.steps_per_character}")

    while (steps := input("\nEnter the new steps per character: ")) or True:
        try:
            steps = int(steps)
            if steps < 1:
                print("Invalid steps per character.")
                continue
        except ValueError:
            print("Invalid steps per character.")
            continue
        break

    enigma.spindle.set_steps_per_character(steps)


def add_plugboard_connection():
    print("Current Plugboard:")
    print(enigma.plugboard)
    for i in range(enigma.plugboard.size + 1, enigma.plugboard.max_plugs + 1):
        print(f"{i}: --EMPTY--")

    while (char_a := input("\nEnter first character: ")) or True:
        if len(char_a) != 1 or char_a not in c.characters:
            print("Invalid character.")
            continue
        if char_a in enigma.plugboard.mapping:
            print("Character already used in plugboard.")
            continue
        break

    while (char_b := input("\nEnter first character: ")) or True:
        if len(char_b) != 1 or char_b not in c.characters:
            print("Invalid character.")
            continue
        if char_b in enigma.plugboard.mapping or char_b == char_a:
            print("Character already used in plugboard.")
            continue
        break

    enigma.plugboard.add_plug(char_a, char_b)


def remove_plugboard_connection():
    if enigma.plugboard.size > 0:
        print("Current Plugboard Connections:")
        print(enigma.plugboard)

        while (position := input("\nSelect a connection to remove: ")) or True:
            try:
                position = int(position)
                if position < 1 or position > enigma.plugboard.size:
                    print("Invalid position.")
                    continue
            except ValueError:
                print("Invalid position.")
                continue
            position -= 1
            break

        enigma.plugboard.remove_plug(enigma.plugboard.pairs.get(position)[0])
    else:
        print("No Plugboard Connections.")


def encrypt():
    for i in range(enigma.spindle.capacity):
        if enigma.spindle.rotors.get(i) is None:
            print("You haven't selected all rotors yet.")
            return
    if enigma.spindle.reflector is None:
        print("You haven't selected the reflector yet.")
        return

    while (text := input("Enter text to encrypt:\n")) or True:
        if any([x not in c.characters for x in text]):
            continue
        break

    print(enigma.encrypt(text))


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError) as err:
        pass
