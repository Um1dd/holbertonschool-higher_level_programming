#!/usr/bin/python3
"""Square sinfi üçün modul."""


class Square:
    """Kvadratı təmsil edən sinif."""

    def __init__(self, size=0, position=(0, 0)):
        """Yeni bir Square obyekti yaradır."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Size dəyərini qaytarır."""
        return self.__size

    @size.setter
    def size(self, value):
        """Size dəyərini yoxlayır və təyin edir."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Position dəyərini qaytarır."""
        return self.__size_position

    @position.setter
    def position(self, value):
        """Position dəyərini yoxlayır və təyin edir."""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size_position = value

    def area(self):
        """Kvadratın sahəsini hesablayır."""
        return self.__size ** 2

    def my_print(self):
        """Kvadratı position nəzərə alaraq # ilə çap edir."""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(self.__size_position[1])]
        for i in range(self.__size):
            print(" " * self.__size_position[0] + "#" * self.__size)
