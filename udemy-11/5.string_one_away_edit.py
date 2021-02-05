7#!/bin/python

def is_one_away(stra, strb):
    if (len(stra) - len(strb)) in [-1, 0, 1]:
        count = 0
        a = 0
        b = 0
        while(a < len(stra) and b < len(strb)):
            if stra[a] != strb[b]:
                count += 1
                if len(stra) >= len(strb):
                    a += 1
                if len(stra) <= len(strb):
                    b += 1
            else:
                a += 1
                b += 1

            if count > 1:
                return False

        return True

    return False

if __name__ == "__main__":
    testa = "pisco"
    testb = "piscol"
    print "String are 1 edit away?: {}".format(is_one_away(testa, testb))
