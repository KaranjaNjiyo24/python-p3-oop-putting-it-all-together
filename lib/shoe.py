#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self._size = size
        self.condition = None

    @property
    def size(self):
        return self._size
