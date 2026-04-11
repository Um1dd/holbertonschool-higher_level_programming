#!/usr/bin/python3
"""Square sinfi üçün modul"""


class Square:
    """Kvadratı təmsil edən sinif"""

    def __init__(self, size=0):
        """Yeni bir Square obyekti yaradır"""
        self.size = size

    @property
    def size(self):
        """Kvadratın ölçüsünü qaytarır"""
        return self.__size

    @size.setter
    def size(self, value):
        """Kvadratın ölçüsünü təyin edir və yoxlayır"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Kvadratın sahəsini hesablayır"""
        return self.__size ** 2

    def my_print(self):
        """Kvadratı # simvolları ilə ekrana çap edir"""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                print("#" * self.__size)
