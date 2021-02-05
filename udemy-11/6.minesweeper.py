#!/bin/python

def mine_sweeper(bombs, rows, cols):
    # board = [[0] * cols] * rows
    board = [[0 for col in range(cols)] for row in range(rows)]
    for bomb in bombs:
        (x, y) = bomb
        print "({}, {})".format(x, y)
        board[x][y] = -1
        for i in range(x -1, x + 2):
            for j in range(y - 1, y + 2):
                if 0 <= i < rows and 0 <= j < cols and board[i][j] != -1:
                    board[i][j] += 1
    return board

if __name__ == "__main__":
    # bombs = [[3, 0], [1, 4]]
    bombs = [[3, 0], [3, 1], [4, 1], [1, 4]]
    ms = mine_sweeper(bombs, 5, 6)
    print "Minesweeper:"
    for row in ms:
        print row
