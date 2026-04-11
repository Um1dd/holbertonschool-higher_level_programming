#!/usr/bin/python3
for letter in range(97, 123):
    if chr(letter) != 'e' and chr(letter) != 'q':
        print("{:s}".format(chr(letter)), end="")
