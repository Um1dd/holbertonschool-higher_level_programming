#!/usr/bin/python3
"""
Bu modul mesajla birlikdə NameError xətası yaradan funksiyanı saxlayır.
"""


def raise_exception_msg(message=""):
    """NameError xətası yaradır və arqument kimi gələn mesajı daxil edir."""
    raise NameError(message)
