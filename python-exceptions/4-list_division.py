#!/usr/bin/python3
"""
Bu modul iki siyahı elementinin bölünməsini təmin edən funksiyanı saxlayır.
"""


def list_division(my_list_1, my_list_2, list_length):
    """
    İki siyahının elementlərini bir-birinə bölərək yeni siyahı yaradır.

    Args:
        my_list_1: Birinci siyahı.
        my_list_2: İkinci siyahı.
        list_length: Yaradılacaq yeni siyahının uzunluğu.

    Returns:
        Bölmə nəticələrini saxlayan yeni siyahı.
    """
    new_list = []
    for i in range(list_length):
        div_result = 0
        try:
            div_result = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            new_list.append(div_result)
    return new_list
