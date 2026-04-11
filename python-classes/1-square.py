#!/usr/bin/python3
"""Square sinfi üçün modul"""


class Square:
    """Kvadratı təmsil edən sinif"""

    def __init__(self, size):
        """
        Yeni bir Square obyekti yaradır.

        Args:
            size: Kvadratın tərəfinin ölçüsü.
        """
        self.__size = size
