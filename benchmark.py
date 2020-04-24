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

    # Loop from 0 to n, step = 1
    for i in range (0,n,1):

        # append generated to list 
        array.append(randint(0,100))
    return array

def algorithm_time(algorithm,input_array):
    ''' Method to benchmarking sorting algorithms.
         

        Parameters:
        -----------
            algorithm: method
                Method of sort algorithm

            input_array: list
                list of generated numbers to be sorted 

        Returns:
        -------
            elapsed_time: int
                Time of running algorithm - Measured in seconds
    '''
   
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
    '''Method is a driver to perform all necessary operations and calculations.


        Returns:
        --------
        algorithm_df: Pandas DataFrame
            method returns pandas dataframe to display results in a nice looking table


    '''
    # each item in input_size list is a number of generated integers by generate_array() method
    input_size = [200,300,500,750,1000,1250,1500,2500, 3750]

    # arrays to store average time results 
    bubble_list = []
    counting_list = []
    merge_list = []
    heap_list = []
    selection_list = []

    # loop over input_size method 
    for n in input_size:
        # each time item taken from input_size list is a parameter of generate_array() method

        input_array = generate_array(n)

        # arrays to store temporary running time values (10 values for each n) for each algorithm -  
        temp_bubble_list = []
        temp_counting_list = []
        temp_merge_list = []
        temp_heap_list = []
        temp_selection_list = []

        # test is carried out 10 times for each n, calls algorithm_time method for each algorithm and result is appended into temporary tables       
        for j in range(10):
            temp_bubble_list.append(algorithm_time(bbl.bubble_sort,input_array))
            temp_counting_list.append(algorithm_time(ctg.counting_sort,input_array))
            temp_merge_list.append(algorithm_time(mrg.merge_sort,input_array))
            temp_heap_list.append(algorithm_time(hep.heap_sort,input_array))
            temp_selection_list.append(algorithm_time(sel.selection_sort,input_array))
        
        # average value is multiplied by 1000 to get milliseconds, rounded to 3 decimal places 
        # and appended into list separately for each algorithm.  
        bubble_list.append(np.around(np.mean(temp_bubble_list)*1000,3))
        counting_list.append(np.around(np.mean(temp_counting_list)*1000,3))
        merge_list.append(np.around(np.mean(temp_merge_list)*1000,3))
        heap_list.append(np.around(np.mean(temp_heap_list)*1000,3))
        selection_list.append(np.around(np.mean(temp_selection_list)*1000,3))

    # For purpose of displaying results in a nice looking way dataframe is created
    algorithm_df = pd.DataFrame()

    # All measuerd running times of sorted algorithms are added to dataframe
    # also input_size list is added (for indexing)  
    algorithm_df['Size'] = input_size
    algorithm_df['Bubble Sort'] = bubble_list
    algorithm_df['Merge Sort'] = counting_list
    algorithm_df['Counting Sort'] = merge_list
    algorithm_df['Heap Sort'] = heap_list
    algorithm_df['Selection Sort'] = selection_list

    # Set 'Size' as an Index 
    algorithm_df.set_index('Size', inplace = True)

    # Return dataframe
    return algorithm_df


def print_df():
    '''Method to display dataframe in console 
        Data Frame is transposed to get algorithm name as a row 
        and input_size as a columns
    '''
    print(main().T)

if __name__ == "__main__":    
# Call print_df() method 
    print_df()

    



