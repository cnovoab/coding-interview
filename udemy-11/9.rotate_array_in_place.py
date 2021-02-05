#!/bin/python

def rotate_array(a, n):
    for layer in range((n // 2)):
        for i in range(layer, n - layer - 1):
            # Top-Left
            aux = a[layer][i]
            # Bottom Left -> Top Left
            a[layer][i] = a[n - i - 1][layer]
            # Bottom Right -> Bottom Left
            a[n - i - 1][layer] = a[n - layer - 1][n - i - 1]
            # Top Right -> Bottom Right
            a[n - layer - 1][n - i - 1] = a[i][n - layer - 1]
            # Top Left -> Top Right
            a[i][n - layer - 1] = aux
    return a

if __name__ == "__main__":
    test = [[1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]]
    print "Original:"
    for row in test:
        print row

    rotate_array(test, len(test))
    print "Rotated:"
    for row in test:
        print row
