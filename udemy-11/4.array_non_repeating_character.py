#!/bin/python

def non_repeating_char(alist):
    unique_items = dict()

    for item in alist:
        if item not in unique_items:
            unique_items[item] = 1
        else:
            unique_items[item] += 1

    for item in alist:
        if unique_items[item] == 1:
            return item

    return None

if __name__ == "__main__":
    # test = [0, 0, 1, 2, 2, 1, 666, 666]
    test = [0, 0]
    print "The first non-repeating char of {} is: {}".format(test, non_repeating_char(test))
