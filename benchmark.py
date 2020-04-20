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


#pd.options.display.float_format = '{:,.3f}'.format

def generate_array(n):
    ''' Method to generate array of random numbers in range from 0 to 100. 

        Parameters:
        -----------
            n: int
                Is a number of items in array / length 

            array: list
                Stores generated numbers 
    '''
    # create empty array
    array = []

    for i in range (0,n,1):
        array.append(randint(0,100))
    return array


def main():
    ''' Method to run benchmark, calculate average time for each algorithm. 

        Parameters:
        -----------
            input_size: list
                !!!

            input_array: list
                Stores result returned by generate_array() method - which is a list of generated integers 

            bubble_out: list
                Stores 10 elapsed times returned from Bubble sort algorithm

            bubble_avg_out: list
                Stores calculated average time for each element from input_size list for Bubble sort algorithm

            bubble_time: float
                Stores returned value of elapsed time from bubble_sort() method
             
            merge_out: list
                Stores 10 elapsed times returned from Merge sort algorithm,

            merge_avg_out: list
                Stores calculated average time for each element from input_size list for Merge sort algorithm         

            
    '''

    input_size = [100,250,500,750,1000,1250,2500,3750]

    bubble_avg_out = []
    merge_avg_out = []
    for i in input_size:
        input_array = generate_array(i)
        
        bubble_out = []
        merge_out = []

        # Loop to 
        for j in range(10):
            # bubble sort 
            bubble_time = bbl.bubble_sort(input_array)
            bubble_out.append(bubble_time)

            # merge sort
            merge_time = mrg.merge_sort(input_array)
            merge_out.append(merge_time)

        bubble_avg_out.append(np.around(np.mean(bubble_out)*1000,3))
        merge_avg_out.append(np.around(np.mean(merge_out)*1000,3))



    algorithm_df = pd.DataFrame(columns = ['Algorithm'] + input_size)
    print (type(algorithm_df))
    algorithm_df.loc['Bubble Sort'] = bubble_avg_out
    algorithm_df.loc['Merge Sort'] = merge_avg_out
     
    return algorithm_df        

    
    

print (main())