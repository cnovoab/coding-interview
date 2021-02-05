#!/bin/python

def rooks_are_safe(board):
    x = dict()
    y = dict()
    for i in range(len(board)):
        x[i] = 0
        for j in range(len(board[i])):
            y[j] = y.get(j, 0)
            if board[i][j] == 1:
                if x[i] > 0:
                    return False
                if y[j] > 0:
                    return False
                x[i] += board[i][j]
                y[j] += board[i][j]

    return True

if __name__ == "__main__":
    test = [[1, 0, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1],
            [0, 1, 0, 1]]
    test = []

    # Print chessboard
    for row in test:
        print row

    print "Rooks are safe?: {}".format(rooks_are_safe(test))
