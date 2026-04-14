#!/usr/bin/python3
"""
Bu modul siyahı elementlərini təhlükəsiz şəkildə çap edən funksiyanı saxlayır.
"""


def safe_print_list(my_list=[], x=0):
    """
    Siyahıdan x sayda elementi çap edir.

    Args:
        my_list: İstənilən tipdə elementləri olan siyahı.
        x: Çap ediləcək elementlərin sayı.

    Returns:
        Həqiqətən çap edilmiş elementlərin sayı.
    """
    count = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            count += 1
        except IndexError:
            break
    print("")  # Sonda yeni sətir
    return count
