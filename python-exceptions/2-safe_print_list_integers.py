#!/usr/bin/python3
"""
Bu modul siyahıdakı tam ədədləri çap edən funksiyanı saxlayır.
"""


def safe_print_list_integers(my_list=[], x=0):
    """
    Siyahının ilk x elementi arasından yalnız tam ədədləri çap edir.

    Args:
        my_list: İstənilən tipdə elementləri olan siyahı.
        x: Giriş ediləcək elementlərin sayı.

    Returns:
        Çap edilmiş tam ədədlərin sayı.
    """
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            continue
    print("")
    return count
