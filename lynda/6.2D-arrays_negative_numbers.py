#!/bin/python

def quadratic(board):
    n = len(board)
    total = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] < 0:
                total += 1
    return total

def linear(board):
    n = len(board)
    total = 0
    row_i = 0
    col_i = n - 1
    while(col_i >= 0 and row_i < n):
        if board[row_i][col_i] < 0:
            total += col_i + 1
            row_i += 1
        else:
            col_i -= 1

    return total

if __name__ == "__main__":
    test = [[-4, -3, -1,  0],
            [-2, -2,  1,  2],
            [-1,  1,  2,  3],
            [ 1,  2,  4,  5]]
#    test = []

    # Print array
    for row in test:
        print row

    print "Quadratic function result: {}".format(quadratic(test))
    print "Linear function result: {}".format(linear(test))
