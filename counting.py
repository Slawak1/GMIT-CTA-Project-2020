# Code taken from https://www.programiz.com/dsa/counting-sort


def counting_sort(array):
    ''' Method to measure time of Counting sort algorithm. Sort in-place. 

        Parameters:
        -----------
            arr: list
                List of numbers generated randomly by randint(0,100)
            
        Returns:
        --------
            arr: list
                returns sorted array
    '''
    #get the max value from the array
    maxval = max(array)
    
    m = maxval + 1
    count = [0] * m               # set all elements in the count array to 0
    for a in array:
        count[a] += 1             # count occurences
    i = 0
    for a in range(m):            # emit
        for c in range(count[a]): # - emit 'count[a]' copies of 'a'
            array[i] = a
            i += 1



    return array



