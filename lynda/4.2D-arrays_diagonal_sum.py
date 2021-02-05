#!/bin/python
'''
You're given a 2D array with the same number of rows and columns. Write a function that adds up the diagonal elements and returns the sum.
For example, you're given the following 2D array:
    [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
The diagonal elements are 1, 5, and 9, so your function should return 15.
'''

def diagonal_sum(array):
    result = 0

    for i in range(len(array)):
        result += array[i][i]

    return result

if __name__ == "__main__":
    test = [[10, 2, 3], [4, 5, 6], [7, 8, 9]]
    print "The diagonal sum of the array is: {}".format(str(diagonal_sum(test)))
