#!/usr/bin/python3
"""program to solve the N queens problem"""


def checkPass(board, row, col):
    '''Checks if matrix is safe from attack
    Args:
        board: The board state.
        row: The row to examine.
        col: The column to colomn.
    '''
    for c in range(col):
        if board[c] is row or abs(board[c] - row) is abs(c - col):
            return False
    return True


def chessBoard(board, col):
    '''Checks the board state column by column using backtracking.
    Args:
        board: The board state.
        col: The current colum to check.
    '''
    colCount = len(board)
    if col is colCount:
        print(str([[c, board[c]] for c in range(colCount)]))
        return

    for row in range(colCount):
        if checkPass(board, row, col):
            board[col] = row
            chessBoard(board, col + 1)


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    num = 0
    try:
        num = int(sys.argv[1])
    except:
        print("N must be a number")
        sys.exit(1)
    if num < 4:
        print("N must be at least 4")
        sys.exit(1)
    board = [0 for col in range(num)]
    chessBoard(board, 0)
