#!/usr/bin/python3
def uppercase(str):
    for h in str:
        upper_c = chr(ord(h) - 32) if 97 <= ord(h) <= 122 else h
        print("{}".format(upper_c), end="")
    print()
