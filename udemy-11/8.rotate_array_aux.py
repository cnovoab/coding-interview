#!/bin/python

def rotate_array(a, n):
    a2 = [[None for i in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            i2 = j
            j2 = n - i - 1
            a2[i2][j2] = a[i][j]
    return a2

if __name__ == "__main__":
    test = [[1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]]
    print "Original:"
    for row in test:
        print row

    rotated_array = rotate_array(test, len(test))
    print "Rotated:"
    for row in rotated_array:
        print row
