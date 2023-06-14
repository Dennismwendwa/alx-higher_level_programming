#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    import hidden_4

for item in dir(hidden_4):
    if item[0] is not '_':
        print("{:s}".format(item))
