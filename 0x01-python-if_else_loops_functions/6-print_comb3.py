#!/usr/bin/python3
for fist in range(10):
    for seco in range(fist + 1, 10):
        print("{:d}{:d}".format(fist, seco), end=", " if fist < 8 else "\n")
