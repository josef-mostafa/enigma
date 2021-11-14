import ctypes


class Array(object):
    def __init__(self, size, default_value=None):
        assert size > 0, "Array size must be > 0"
        self._size = size
        self._default_value = default_value
        PyArrayType = ctypes.py_object * size
        self._elements = PyArrayType()
        self._itemCount = 0
        self.reset()

    def __len__(self):
        return self._size

    def __print__(self):
        for i in range(self._itemCount):
            print(self._elements[i], end=" ")

    def reset(self):
        for i in range(self._size):
            self._elements[i] = self._default_value
        self._itemCount = 0

    def insert(self, item):
        if self._size > self._itemCount:
            self._elements[self._itemCount] = item
            self._itemCount += 1
        else:
            print("Array is full")

    def get(self, index):
        return self._elements[index]

    def remove_at(self, index):
        self._itemCount -= 1
        for i in range(index, self._itemCount):
            self._elements[i] = self._elements[i+1]
        self._elements[self._itemCount] = self._default_value

    def remove(self, item):
        for i in range(self._itemCount):
            if self._elements[i] == item:
                self.remove_at(i)
                break

    def contains(self, term):
        for i in range(self._itemCount):
            if self._elements[i] == term:
                return True
        return False

    def set_item(self, position, item):
        if position >= 0 and position < self._size:
            self._elements[position] = item
        else:
            print("Invalid position")


class _MapEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return str(str(self.key)+" : " + str(self.value))


class Map:
    def __init__(self, size):
        self._entryList = Array(size)
        self._size = size
        self._entryCount = 0

    def insert(self, key, value):
        for i in range(self._entryCount):
            if self._entryList.get(i).key == key:
                print("Key already exists")
                return
        if self._size > self._entryCount:
            entry = _MapEntry(key, value)
            self._entryList.insert(entry)
            self._entryCount += 1
        else:
            print("Map is full")

    def get(self, key):
        for i in range(self._entryCount):
            if self._entryList.get(i).key == key:
                return self._entryList.get(i).value

    def remove(self, key):
        for i in range(self._entryCount):
            if self._entryList.get(i).key == key:
                self._entryList.remove_at(i)
                self._entryCount -= 1
                break

    def contains(self, key):
        for i in range(self._entryCount):
            if self._entryList.get(i).key == key:
                return True
        return False
