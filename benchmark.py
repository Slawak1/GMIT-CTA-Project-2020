# Computational Thinking With Algorithms
# Project: Benchmarking Sorting Algorithms
# Slawomir Sowa
# 13.04.2020


from random import randint
import time

def main():
    pass


def generate_array(n):

    array = []
    for i in range (0,n,1):
        array.append(randint(0,100))
    return array

def bubble_sort(arr): 
    start_time = time.time()
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
    end_time = time.time()
    time_elapsed = end_time - start_time
    return time_elapsed

def main():

    input_size = [250,500,750,1000,1250,2500]
    output_arr = []
    for i in input_size:
        out = bubble_sort(generate_array(i))
        output_arr.append(out)
    
    print(output_arr)
    

main()