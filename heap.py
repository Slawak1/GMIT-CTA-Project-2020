# code taken from https://www.educative.io/edpresso/how-to-implement-heap-sort



def heapify(arr, n, i): 
    ''' Method to build a heap.
        Parameters:
        ----------
            arr: list
                list of numbers to be sorted

            i: int
                index
            
            n: int
                heap size
    '''
    # set largest as root
    largest = i 
    l = 2 * i + 1     # left = 2*i + 1 
    r = 2 * i + 2     # right = 2*i + 2 
  
    # Compare left child of root 
    if (l < n and arr[i] < arr[l]): 
        largest = l 
  
    # Compare left child of root 
    if (r < n and arr[largest] < arr[r]): 
        largest = r 
  
    # Swap nodes, if needed 
    if (largest != i): 
        arr[i],arr[largest] = arr[largest],arr[i] # swap 
  
        # Heapify the root. 
        heapify(arr, n, largest) 
  
 
def heap_sort(arr): 
    ''' Method to sort an array.
        Parameters:
        ----------
            arr: list
                list of numbers to be sorted
    '''
    # get length of a list 
    n = len(arr) 
  
    # Build a heap. 
    for i in range(n, -1, -1): 
        heapify(arr, n, i) 
  
    # One by one extract elements 
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i] # swap 
        heapify(arr, i, 0) 


    return arr

