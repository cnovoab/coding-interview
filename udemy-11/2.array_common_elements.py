#!/bin/python

def common_items(alist, blist):
    common = []
    n = 0
    m = 0
    while(n < len(alist) and m < len(blist)):
        if alist[n] == blist[m]:
            common.append(alist[n])
            m += 1
            n += 1
        elif alist[n] > blist[m]:
            m += 1
        else:
            n += 1

    return common

if __name__ == "__main__":
    testa = [1, 3, 7, 34, 35]
    testb = [1, 2, 5, 7, 9, 35]
    print "Common elements between {} and {} are: {}".format(testa, testb, common_items(testa, testb))
