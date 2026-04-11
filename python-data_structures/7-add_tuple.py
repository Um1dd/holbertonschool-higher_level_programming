#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Hər tuple üçün ilk iki elementi təmin edirik (çatışmırsa 0 əlavə edirik)
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)
    
    # Yeni tuple yaradırıq: ilk iki elementin cəmi
    result = (a[0] + b[0], a[1] + b[1])
    
    return result
