# Code taken from https://www.programiz.com/dsa/counting-sort


# Counting sort in Python programming


def counting_sort(array):



    maxval = max(array)
    #n = len(array)
    m = maxval + 1
    count = [0] * m               # init with zeros
    for a in array:
        count[a] += 1             # count occurences
    i = 0
    for a in range(m):            # emit
        for c in range(count[a]): # - emit 'count[a]' copies of 'a'
            array[i] = a
            i += 1



    return array

