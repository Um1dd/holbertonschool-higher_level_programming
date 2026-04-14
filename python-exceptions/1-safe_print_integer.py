#!/usr/bin/python3
"""
Bu modul tam ədədlərin təhlükəsiz çapı üçün funksiyanı saxlayır.
"""


def safe_print_integer(value):
    """
    Dəyəri integer formatında çap edir.

    Args:
        value: Çap ediləcək istənilən tipdə dəyər.

    Returns:
        True əgər uğurla çap edildisə, False əks halda.
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
