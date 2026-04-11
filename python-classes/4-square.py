#!/usr/bin/python3
"""
Bu modul Square sinfini təyin edir.
"""


class Square:
    """
    Kvadratı təmsil edən sinif.
    """

    def __init__(self, size=0):
        """
        Yeni bir Square obyekti yaradır.

        Args:
            size (int): Kvadratın tərəfinin ölçüsü.
        """
        self.size = size

    @property
    def size(self):
        """
        Kvadratın ölçüsünü qaytarır (Getter).
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Kvadratın ölçüsünü təyin edir və yoxlayır (Setter).

        Args:
            value (int): Yeni ölçü dəyəri.

        Raises:
            TypeError: Əgər dəyər integer deyilsə.
            ValueError: Əgər dəyər 0-dan kiçikdirsə.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Kvadratın sahəsini hesablayır.

        Returns:
            int: Sahə dəyəri.
        """
        return self.__size ** 2
