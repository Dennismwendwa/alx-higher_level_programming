#!/usr/bin/python3
"""
This module resolves the N-Queen puzzle using backtracting
"""


from sys import argv

if __name__ == "__main__":
    m = []
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if argv[1].isdigit() is False:
        print("N must be a number")
        exit(1)
    n = int(argv[1])
    if n < 4:
        print("N must be at least 4")
        exit(1)

    for j in range(n):
        m.append([j, None])

    def ready_exist(h):
        """check the queen already exist"""
        for x in range(n):
            if h == m[x][1]:
                return True
        return False

    def rejectie(x, h):
        """determines whether or not the solution will reject"""
        if (ready_exist(h)):
            return False
        j = 0
        while (j < x):
            if abs(m[j][1] - h) == abs(j - x):
                return False
            j += 1
        return True

    def clear_m(x):
        """clears from the failure"""
        for j in range(x, n):
            m[j][1] = None

    def nqueens(x):
        """recurssive backtracking"""
        for h in range(n):
            clear_m(x)
            if rejectie(x, h):
                m[x][1] = h
                if (x == n - 1):
                    print(a)
                else:
                    nqueens(x + 1)

    nqueens(0)
