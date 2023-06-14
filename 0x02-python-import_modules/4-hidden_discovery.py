#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    import hidden_4

objects = list(dir(hidden_4))

for item in objects:
    if item[0] is not "_":
        print("{:s}".format(item))
