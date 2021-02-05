#!/bin/python

def sums(alist, sum = 10):
    visited = dict()
    for number in alist:
        search = sum - number
        print "Number: {} - Search: {}".format(number, search)
        if search in visited:
            return [search, number]

        visited[number] = 1

    return None

if __name__ == "__main__":
    test = [1, 2, 4, 6, 8]
    assert(1, 10)
    print "Pair of numbers that sums up 10: {}".format(sums(test))
