
# code taken from https://www.geeksforgeeks.org/bubble-sort/


def bubble_sort(arr): 
    ''' Method to measure time of Bubble sorting algorithm. 

        Parameters:
        -----------
            arr: list
                List of numbers generated randomly by randint(0,100)
            
        Returns:
        --------
            arr: list
                returns sorted array
    '''

    n = len(arr) 

    # Traverse through all array elements 
    for i in range(n): 

    # Last i elements are already in place 
        for j in range(0, n-i-1): 

            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 

    return arr

