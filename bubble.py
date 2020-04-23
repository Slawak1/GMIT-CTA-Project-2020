
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
    # length of the array assigned to variable 
    n = len(arr) 

    # Loop over all array elements 
    for i in range(n): 

    # After each iteration the largest element is placed at the end
        for j in range(0, n-i-1): 

            # Swap if the element arr[j]is greater than arr[j+1]
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
    
    # return sorted array
    return arr

