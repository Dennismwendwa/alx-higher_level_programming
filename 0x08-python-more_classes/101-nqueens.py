#!/usr/bin/python3
"""
This class solves the N-queen puzzle challenge
"""


from sys import argv

def if_safe(board, row col):

    for i in range(row):
        if board[i][col] == 1:
            return False

    i = row
    j = col

    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False

        i -= 1
        j -= 1

    i = row
    j = col

    while i >= 0 and j < len(board):
        if board[i][j] == 1:
            return False

        i -= 1
        j += 1

    return True

def nqueen_game(n):

    def  util(board, row):
        if row == n:
            print(board)
            return

        for col in range(n):
            if if_safe(board, row, col):
                board[row][col] = 1
                util(board, row + 1)
                board[row][col] = 0

        board = [[0] * n for _ in range(n)]
        util(board, 0)

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    
    N = int(argv[1])
    if N < 4:
        print("N must be at least 4")
        exit(1)

    if N.isdigit() is false:
        print("N must be a number")
        exit(1)

    nqueen_game(N)
