#!/usr/bin/python3

"""Define a class Square"""


class Square:
    """Rpresent a square."""
    def __init__(self, size=0):
        """ Initialize  new square"""
        self.size = size

    @property
    def size(self):
        """Get size of the square"""
        return(self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be greater than or 0")
        self.__size = value

    def area(self):
        """Return area"""
        return (self.__size * self.__size)
