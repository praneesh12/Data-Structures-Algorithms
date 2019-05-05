# Selection sort
# Intuition : Sort an array by finding the min of the array and storing it in temp_array
# Repeat until list is sorted

from random import randint
def create_random_array(length=10, maxint=50):
	return [randint(0, maxint) for _ in range(length)]

def selectionSort(array):
	return_array = []

	while len(array)>0:

		min_element = min(array)
		return_array.append(min_element)
		array.remove(min_element)
	return return_array

array = create_random_array()
print('Random array before sorting \n{}\n'.format(array))
print('Random array after sorting \n{}'.format(selectionSort(array)))