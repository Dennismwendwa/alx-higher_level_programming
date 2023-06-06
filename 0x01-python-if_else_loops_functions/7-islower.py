#!/usr/bin/python3
def islower(c):
    lowercase_range = range(ord("a"), ord("z") + 1)
    if ord(c) in lowercase_range:
        return True
    else:
        return False
