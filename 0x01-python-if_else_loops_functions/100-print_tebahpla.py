#!/usr/bin/python3
for lettr in range(122, 96, -1):
    if lettr % 2 != 0:
        lettr = lettr - 32
    print("{}".format(chr(lettr)), end="")
