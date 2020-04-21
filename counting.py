# Code taken from https://www.programiz.com/dsa/counting-sort

import time

# Counting sort in Python programming


def counting_sort(array):

    start_time = time.time()

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


    end_time = time.time()  
    time_elapsed = (end_time - start_time)

    return time_elapsed

