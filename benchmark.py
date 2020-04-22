# Computational Thinking With Algorithms
# Project: Benchmarking Sorting Algorithms
# Slawomir Sowa
# 13.04.2020


from random import randint
import time
import numpy as np
import pandas as pd
import bubble as bbl
import merge as mrg
import counting as ctg
import heap as hep
import selection as sel


def generate_array(n):
    ''' Method to generate array of random numbers in range from 0 to 100. 

        Parameters:
        -----------
            n: int
                Is a number of items in array / length 

        Returns:
        -------
            list
                a list of randomly generated numbers from 0 to 99 

    '''
    # create empty array
    array = []

    # Loop from 0 to n 
    for i in range (0,n,1):
        array.append(randint(0,100))
    return array

def algorithm_time(algorithm,input_array):
    ''' Method to generate array of random numbers in range from 0 to 100. 

        Parameters:
        -----------
            algorithm: method
                Method of sort algorithm

            input_array: list
                list of generated numbers to be sorted 

        Returns:
        -------
            elapsed_time: int
                Measured in seconds
    '''

    for i in range(10):
        # starting the clock
        start_time = time.time()
        
        # sorting algorithm 
        algorithm(input_array)
        
        # stop the clock
        end_time = time.time()
        
        # calculate elapsed time 
        time_elapsed = (end_time - start_time)
    return time_elapsed


def main():
    input_size = [200,300,500,750,1000,1250,1500,2500,3750]

    # arrays to store time results 
    bubble_list = []
    counting_list = []
    merge_list = []
    heap_list = []
    selection_list = []

    for n in input_size:
        input_array = generate_array(n)

        temp_bubble_list = []
        temp_counting_list = []
        temp_merge_list = []
        temp_heap_list = []
        temp_selection_list = []

        # start test 10 times and calculate average 
        for j in range(10):
            temp_bubble_list.append(algorithm_time(bbl.bubble_sort,input_array))
            temp_counting_list.append(algorithm_time(ctg.counting_sort,input_array))
            temp_merge_list.append(algorithm_time(mrg.merge_sort,input_array))
            temp_heap_list.append(algorithm_time(hep.heap_sort,input_array))
            temp_selection_list.append(algorithm_time(sel.selection_sort,input_array))
        
        bubble_list.append(np.around(np.mean(temp_bubble_list)*1000,3))
        counting_list.append(np.around(np.mean(temp_counting_list)*1000,3))
        merge_list.append(np.around(np.mean(temp_merge_list)*1000,3))
        heap_list.append(np.around(np.mean(temp_heap_list)*1000,3))
        selection_list.append(np.around(np.mean(temp_selection_list)*1000,3))



    #-------------------------------------------------# 
    #Create Dataframe 
    algorithm_df = pd.DataFrame()

    # Add measuerd times of sorted algorithms to dataframe  
    algorithm_df['Size'] = input_size
    algorithm_df['Bubble Sort'] = bubble_list
    algorithm_df['Merge Sort'] = counting_list
    algorithm_df['Counting Sort'] = merge_list
    algorithm_df['Heap Sort'] = heap_list
    algorithm_df['Selection Sort'] = selection_list

    # Set 'Size' as an Index 
    algorithm_df.set_index('Size', inplace = True)
    

    # Return Transposed dataframe for better view
    return algorithm_df       


print (main())

    


