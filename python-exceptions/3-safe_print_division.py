#!/usr/bin/python3
"""
Bu modul iki tam ədədin təhlükəsiz bölünməsini təmin edir.
"""


def safe_print_division(a, b):
    """
    a-nı b-yə bölür və nəticəni finally blokunda çap edir.

    Args:
        a (int): Bölünən.
        b (int): Bölən.

    Returns:
        Bölmənin nəticəsi və ya None (əgər 0-a bölünmə baş verərsə).
    """
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        pass
    finally:
        print("Inside result: {}".format(result))
    return result
