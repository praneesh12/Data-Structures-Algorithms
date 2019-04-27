#binary_serach.py Iterative Version 
def binary_search_iterative(input_array, value):
    low_index = 0
    high_index = len(input_array) - 1
    while low_index <= high_index:
        middle_index = (low_index + high_index)//2 # rounds off to lower middle element
        if value == input_array[middle_index]:
        	print('Search value {} found at index {}'.format(value, input_array.index(value)))
        	return True
        elif value < input_array[middle_index]:
            high_index = middle_index - 1
        else:
            low_index = middle_index + 1
  
    print('Search value {} not found'.format(value))
    return False

binary_search_iterative(input_array=[1,2,3,4,5,7,8,9,12,22,34,36], value=6500)