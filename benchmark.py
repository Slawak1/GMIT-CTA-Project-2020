# Computational Thinking With Algorithms
# Project: Benchmarking Sorting Algorithms
# Slawomir Sowa
# 13.04.2020


from random import randint
import time
import numpy as np
import pandas as pd
import bubble as bbl


pd.options.display.float_format = '{:,.3f}'.format

def generate_array(n):

    array = []
    for i in range (0,n,1):
        array.append(randint(0,100))
    return array


def main():

    input_size = [100,250,500,750,1000,1250]
    
    bubble_avg_out = []
    for i in input_size:
        input_array = generate_array(i)
        bubble_out = []
        for j in range(10):
            x = bbl.bubble_sort(input_array)
            x = np.around(x * 1000,3)
            
            bubble_out.append(x)
        bubble_avg_out.append(np.mean(bubble_out))

    



    print (bubble_avg_out)

    algorithm_df = pd.DataFrame(columns = input_size)
    algorithm_df.loc['Bubble Sort'] = bubble_avg_out
    #algorithm_df =  (algorithm_df * 1000).round(3)
 
    print (algorithm_df)        

    
    

main()