#!/bin/python
'''
Input: a and b are numbers as strings
Output: True if a is larger than b, False otherwise
'''

def str_larger_than(num_a, num_b):
    num_a = remove_leading_zeroes(num_a)
    num_b = remove_leading_zeroes(num_b)
    print "Sanitized A: {} - B: {}".format(num_a, num_b)
    if len(num_a) > len(num_b):
        return True
    elif len(num_b) > len(num_a):
        return False
    else:
        for i in range(len(num_a)):
            if num_a[i] == num_b[i]:
                continue
            elif num_a[i] > num_b[i]:
                return True
            else:
                return False

        return False

def remove_leading_zeroes(num):
    new_num = []
    not_zero_found = False
    for i in range(len(num)):
        if num[i] != "0":
            not_zero_found = True

        if not_zero_found:
            new_num.append(num[i])

    if not new_num:
        return "0"

    return ''.join(new_num)

if __name__ == "__main__":
    testa = "0003220"
#    testb = "0000000000000"
#    testb = "0003220"
    testb = "0"
    print "{} is larger than {}?: {}".format(testa, testb, str_larger_than(testa, testb))
