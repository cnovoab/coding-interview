#!/bin/python

def are_reverses(astring, bstring):
    for i in range(len(astring)):
        if astring[i] != bstring[len(astring) - i - 1]:
            return False

    return True

if __name__ == "__main__":
    testa = 'alaska'
    #testb = 'alaska'
    testb = 'aksala'
    print "Are {} and {} reverses of each other?: {}".format(testa, testb, str(are_reverses(testa, testb)))
