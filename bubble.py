
# code taken from https://www.geeksforgeeks.org/bubble-sort/




def bubble_sort(arr): 
    ''' Method to measure time of Bubble sorting algorithm. 

        Parameters:
        -----------
            arr: list
                List of numbers generated randomly by randint(0,100)
            
            start_time: float
                time shown in seconds since the epoch - start time of algorithm

            end_time: float
                time shown in seconds since the epoch - end time of algorithm
            
            time_elapsed: float
                difference between end_time and start_time measured in seconds 



    '''
    #start_time = time.time()
    
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
    #end_time = time.time()
    #time_elapsed = (end_time - start_time)

    return arr

