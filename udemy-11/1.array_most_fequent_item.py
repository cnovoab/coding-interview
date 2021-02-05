#!/bin/python

def most_frequent_item(alist):
    max_count = 0
    max_item = None
    visited = dict()

    for item in alist:
        if item not in visited:
            visited[item] = 1
        else:
            visited[item] += 1

        if visited[item] > max_count:
            max_count = visited[item]
            max_item = item

    return max_item

if __name__ == "__main__":
    test = [1, 3, 1, 3, 2, 1, 3, 3] # -> 1
    print "The most frequent item in the array is: {}".format(most_frequent_item(test))
