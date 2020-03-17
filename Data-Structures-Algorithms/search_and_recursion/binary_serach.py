#binary_serach.py Iterative Version 

import logging

logger = logging.getLogger(__name__)

def binary_search_iterative(input_array, value):
	try:
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
	except Exception as e:
		logging.info('Error message: {}')
		# print('Search value {} not found'.format(value))
        # return False


