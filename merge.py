
# code taken from https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-8.php
from random import randint
import time
import numpy as np

def merge_sort(arr):

    ''' Method to measure time of Merge sorting algorithm. 

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


    start_time = time.time()
    if len(arr)>1:
        mid = len(arr)//2
        lefthalf = arr[:mid]
        righthalf = arr[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)
        i=j=k=0       
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                arr[k]=lefthalf[i]
                i=i+1
            else:
                arr[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            arr[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            arr[k]=righthalf[j]
            j=j+1
            k=k+1
    end_time = time.time()  
    time_elapsed = (end_time - start_time)      
    return time_elapsed
    
