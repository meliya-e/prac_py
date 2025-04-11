class Vowel:
    __slots__ = ("a", "o", "u", "i", "e", "y")
    def __init__(self, **kwargs):
        for key in kwargs:
            if key in self.__slots__:
                setattr(self, key, kwargs[key])

    def __str__(self):
        fill_sl = {k: getattr(self, k) for k in sorted(self.__slots__) if hasattr(self, k)}
        return ", ".join(f"{key}: {fill_sl[key]}" for key in fill_sl)

    @property
    def answer(self):
        return 42

    @property
    def full(self):
        return all(hasattr(self, slot) for slot in self.__slots__)

    @full.setter
    def full(self, val): pass

import sys
exec(sys.stdin.read())
