
# Code taken from https://stackabuse.com/sorting-algorithms-in-python/

def merge(left_list, right_list):

    ''' Method to merge each half that was split, sorting them in the process

        Parameters:
        -----------
            left_list: list
                One of two Lists returned by merge_sort method
            -------
            right_list: list
                Second of two Lists returned by merge_sort method
            
        Returns:
        --------
            sorted_list: list
                returns sorted array
    '''
    sorted_list = []
    left_list_index = right_list_index = 0

    # Create Variables
    left_list_length = len(left_list)
    right_list_length = len(right_list)

    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            # We check which value from the start of each list is smaller
            # If the item at the beginning of the left list is smaller, add it
            # to the sorted list
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            # If the item at the beginning of the right list is smaller, add it
            # to the sorted list
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1

        # If we've reached the end of the of the left list, add the elementsgit s
        # from the right list
        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        # If we've reached the end of the of the right list, add the elements
        # from the left list
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1

    # final result of the sorting
    return sorted_list



def merge_sort(array):
    ''' Method to to divide (sub)arrays into halves and sort them recursively.

        Parameters:
        -----------
            arr: list 
                List of numbers to be sorted
            
        Returns:
        --------
            calling the merge method with two lists as an arguments
    '''
    # If the list is a single element, return it
    if len(array) <= 1:
        return array

    # Use floor division to get midpoint, indices must be integers
    mid = len(array) // 2

    # Sort and merge each half
    left_list = merge_sort(array[:mid])
    right_list = merge_sort(array[mid:])

    # Merge the sorted lists into a new one
    return merge(left_list, right_list)
