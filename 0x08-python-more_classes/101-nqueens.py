#!/usr/bin/python3
"""
This class solves the N-queen puzzle challenge
"""


from sys import argv

if __name__ == "__main__":

    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    if not argv[1].isdigit():
        print("N must be a number")
        exit(1)

    n = int(argv[1])
    if n < 4:
        print("N must be at least 4")
        exit(1)

    choice = []
    for f in range(n):
        choice.append([f, None])

    """check status of the queen"""
    def status(y):
        for z in range(n):
            if y == choice[z][1]:
                return True
            else:
                return False

    """checking the status of the solution at hand"""
    def solution_sts(z, y):
        if (status(y)):
            return False

        w = 0
        while (w < z):
            if abs(choice[w][1] - y) == abs(w - z):
                return False

            w += 1
        return True

    """We empty the choice list here"""
    def empty_choice(z):
        for w in range(z, n):
            choice[w][1] = None

    """we are selecting all possible choices"""
    def tracker(z):
        for y in range(n):
            empty_choice(z)
            if solution_sts(z, y):
                choice[z][1] = y
                if (z == n - 1):
                    print(a)
                else:
                    tracker(z + 1)

        tracker(0)
