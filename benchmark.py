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


#pd.options.display.float_format = '{:,.3f}'.format

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


def main():
    ''' Method to run benchmark, calculate average time for each algorithm. 

        Parameters:
        -----------

        Returns:
        --------
            Pandas DataFrame
                Method to return pandas dataframe    

            
    '''

    input_size = [100,250,500,750,1000,1250,2500,3750]

    bubble_avg_out = []
    merge_avg_out = []
    counting_avg_out = []
    for i in input_size:
        input_array = generate_array(i)
        
        bubble_out = []
        merge_out = []
        counting_out = []

        # Loop to 
        for j in range(10):
            # bubble sort algorithm
            bubble_time = bbl.bubble_sort(input_array)
            bubble_out.append(bubble_time)

            # merge sort algorithm
            merge_time = mrg.merge_sort(input_array)
            merge_out.append(merge_time)

            # counting sort algorithm 

            counting_time = ctg.counting_sort(input_array)
            counting_out.append(counting_time)


        # convert seconds to Milliseconds By multiplying it by 1000 and round to 3 decimal places 
        bubble_avg_out.append(np.around(np.mean(bubble_out)*1000,3))
        merge_avg_out.append(np.around(np.mean(merge_out)*1000,3))
        counting_avg_out.append(np.around(np.mean(counting_out)*1000,3))

    # Create Dataframe 
    algorithm_df = pd.DataFrame()
    algorithm_df['Size'] = input_size
    algorithm_df['Bubble Sort'] = bubble_avg_out
    algorithm_df['Merge Sort'] = merge_avg_out
    algorithm_df['Counting Sort'] = counting_avg_out

    # Set 'Size' as an Index 
    algorithm_df.set_index('Size', inplace = True)
    print (algorithm_df.T)

    # Return Transposed dataframe for better view
    return algorithm_df.T        


    
    
    

