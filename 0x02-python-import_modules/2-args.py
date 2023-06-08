#!/usr/bin/python3

if __name__ == "__main__":
    import sys


if len(sys.argv) == 2:
    print("{:d} argument:".format((len(sys.argv) - 1)))
    print("{:d}: {:s}".format((len(sys.argv) - 1), sys.argv[- 1]))
elif len(sys.argv) == 1:
    print("{:d} arguments.".format(len(sys.argv) - 1))
elif len(sys.argv) > 2:
    print("{:d} arguments:".format(len(sys.argv) - 1))

    f = 1
    while f != len(sys.argv):
        print("{:d}: {}".format(f, sys.argv[f]))
        f += 1
