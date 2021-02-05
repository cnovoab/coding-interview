def second_largest(alist):
    largest = None
    second_largest = None
    for element in alist:
        if largest is None:
            largest = element
        else:
            if element > largest:
                second_largest = largest
                largest = element
            elif element > second_largest:
                second_largest = element

    return second_largest

if __name__ == "__main__":
    #test = [1, 3, 4, 5, 0, 2]
    #test = [5, 1, 3, 4, 5, 0, 0, 2]
    #test = []
    test = [1]
    print "second_largest: {}".format(str(second_largest(test)))
