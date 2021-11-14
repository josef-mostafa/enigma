import unittest
import uuid

from datastructs import Array, Map
from enigma import Enigma
from mappings import ReflectorTypes, RotorTypes


class DataStructsTest(unittest.TestCase):
    """
        Testing the data structures.
    """

    def test_array_get(self):
        array = Array(10, 0)
        self.assertEqual(array.get(0), 0)

    def test_array_insert(self):
        array = Array(10)
        for i in range(10):
            s = str(uuid.uuid4())
            array.insert(s)
            self.assertEqual(array.get(i), s)

    def test_array_set_item(self):
        array = Array(10, "")
        for i in range(10):
            s = str(uuid.uuid4())
            array.set_item(i, s)
            self.assertEqual(array.get(i), s)

    def test_array_remove_at(self):
        array = Array(10)
        for i in range(10):
            array.insert(i)
        array.remove_at(0)
        array.remove_at(0)
        self.assertEqual(len(array), 8)
        for i in range(2, 10):
            self.assertEqual(array.get(i-2), i)

    def test_array_remove(self):
        array = Array(10)
        for i in range(10):
            array.insert(i)
        array.remove(0)
        array.remove(1)
        self.assertEqual(len(array), 8)
        for i in range(2, 10):
            self.assertEqual(array.get(i-2), i)

    def test_array_contains(self):
        array = Array(10)
        for i in range(10):
            self.assertFalse(array.contains(i))
        for i in range(10):
            array.insert(i)
        for i in range(10):
            self.assertTrue(array.contains(i))

    def test_map_insert_and_get(self):
        map = Map(10)
        for i in range(10):
            map.insert(i, -1 * i)
            self.assertEqual(map.get(i), -1 * i)

    def test_map_remove(self):
        map = Map(10)
        for i in range(10):
            map.insert(i, -1 * i)
        map.remove(0)
        map.remove(1)
        self.assertEqual(len(map), 8)
        self.assertFalse(map.contains(0))
        self.assertFalse(map.contains(1))
        for i in range(2, 10):
            self.assertEqual(map.get(i), -1 * i)

    def test_map_contains(self):
        map = Map(10)
        for i in range(10):
            self.assertFalse(map.contains(i))
        for i in range(10):
            map.insert(i, i)
        for i in range(10):
            self.assertTrue(map.contains(i))


class TestEnigma(unittest.TestCase):
    """
        Testing the enigma.
    """

    def test_enigma_encrypt(self):
        e = Enigma()
        e.spindle.set_rotor(RotorTypes.I.value, 0)
        e.spindle.set_rotor(RotorTypes.II.value, 1)
        e.spindle.set_rotor(RotorTypes.III.value, 2)
        e.spindle.set_reflector(ReflectorTypes.A.value)
        e.plugboard.add_plug("A", "B")
        e.plugboard.add_plug("F", "G")
        e.plugboard.add_plug("O", "P")
        e.plugboard.add_plug("U", "V")
        e.spindle.set_steps_per_character(12)
        s = e.encrypt("HELLOWORLD")
        e.spindle.reset_rotors()
        self.assertTrue(e.encrypt(s) == "HELLOWORLD")

    def test_spindle_encrypt(self):
        e = Enigma()
        e.spindle.set_rotor(RotorTypes.I.value, 0)
        e.spindle.set_rotor(RotorTypes.II.value, 1)
        e.spindle.set_rotor(RotorTypes.III.value, 2)
        e.spindle.set_reflector(ReflectorTypes.A.value)
        e.spindle.set_steps_per_character(120)
        e.encrypt("HELLOWORLD")
        self.assertEqual(e.spindle.rotor_offsets.get(0), 23)
        self.assertEqual(e.spindle.rotor_offsets.get(1), 21)
        self.assertEqual(e.spindle.rotor_offsets.get(2), 2)

    def test_plugboard_encrypt(self):
        e = Enigma()
        e.plugboard.add_plug("A", "B")
        e.plugboard.add_plug("F", "G")
        e.plugboard.add_plug("O", "P")
        e.plugboard.add_plug("U", "V")
        sp = "AABBCCDDEEFFGGHHIIJJKKLLMMNNOOPPQQRRSSTTUUVVWWXXYYZZ"
        sc = "BBAACCDDEEGGFFHHIIJJKKLLMMNNPPOOQQRRSSTTVVUUWWXXYYZZ"
        self.assertEqual(e.plugboard.encrypt(sp), sc)


if __name__ == "__main__":
    t = DataStructsTest()
    t.test_map_remove()
    unittest.main()
