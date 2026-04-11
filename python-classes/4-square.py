#!/usr/bin/python3
"""Square sinfi üçün modul"""


class Square:
    """Kvadratı təmsil edən sinif"""

    def __init__(self, size=0):
        """
        Yeni bir Square obyekti yaradır.

        Args:
            size (int): Kvadratın tərəfinin ölçüsü (default 0).
        """
        self.size = size

    @property
    def size(self):
        """Kvadratın ölçüsünü qaytarır (Getter)"""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Kvadratın ölçüsünü təyin edir (Setter).
        
        Args:
            value (int): Yeni ölçü dəyəri.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Kvadratın sahəsini hesablayır və qaytarır"""
        return self.__size ** 2
