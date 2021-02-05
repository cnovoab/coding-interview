#!/bin/python

def is_rotation(alist, blist):
    if len(alist) == len(blist):
        i = 0
        j = 0
        while(j < len(blist) and blist[j] != alist[i]):
            j += 1

        if j >= len(blist):
            return False

        new_blist = blist[j:] + blist[:j]
        for i in range(len(alist)):
            if alist[i] != new_blist[i]:
                return False

        return True

    return False
if __name__ == "__main__":
    testa = [1, 2, 3, 4, 5, 6]
    testb = [5, 6, 0, 2, 3, 6]
    print "A is rotation of B?: {}".format(is_rotation(testa, testb))
