#!/usr/bin/python3
"""Class Square that defines a square with size,
   validation and area method."""


class Square:
    """Class Square that defines a square with size,
       validation and area method."""

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        return self.__size**2

    def my_print(self):
        if self.__size == 0:
            print()
        for column in range(self.__size):
            for line in range(self.__size):
                print("#", end='')
            print()
