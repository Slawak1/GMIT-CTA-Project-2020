# https://stackabuse.com/sorting-algorithms-in-python/

def selection_sort(arr): 
    ''' Method to measure time of Selection sort algorithm. 

        Parameters:
        -----------
            arr: list
                List of numbers generated randomly by randint(0,100)
            
        Returns:
        --------
            arr: list
                returns sorted array
    '''
    for i in range(len(arr)):
        # We assume that the first item of the unsorted segment is the smallest
        lowest_value_index = i
        # This loop iterates over the unsorted items
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[lowest_value_index]:
                lowest_value_index = j
        # Swap values of the lowest unsorted element with the first unsorted
        # element
        arr[i], arr[lowest_value_index] = arr[lowest_value_index], arr[i]

    return arr