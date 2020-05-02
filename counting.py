# Code taken from https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-10.php


def counting_sort(array):
    ''' Method to sort array using Counting Sort Algorithm.

        Parameters:
        -----------
            arr: list
                List of numbers to be sorted
            
        Returns:
        --------
            arr: list
                returns sorted array
    '''
    #get the max value from the array
    maxval = max(array)
    
    # adding 1 to max value m
    m = maxval + 1

    # set all elements in the count array to 0
    count = [0] * m    

    # checking each element in array and counts how many times element occurs            
    for a in array:
        count[a] += 1             

    # sort in place, copy back into original list   
    i = 0
    for a in range(m):            
        for c in range(count[a]): 
            array[i] = a
            i += 1
            
    # return sorted array
    return array



