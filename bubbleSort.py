# Sorting Algorithm Naive approach : Bubble Sort
# Runtime 
# array = [132,143,156,169,172,34,44,55,56,76,87,98,172,1,3,4,8,12,122,188,234,122,132,143,156,169]

#Create a randomized array of length 'length' and range 0,maxint
from random import randint


def create_random_array(length=10, maxint=50):
	return [randint(0, maxint) for _ in range(length)]

def bubbleSort(array):
	swapped=True
	while swapped:
		swapped=False
		for i in range(1,len(array)):
			if array[i-1] > array[i]:
				array[i],array[i-1] = array[i-1],array[i]
				swapped=True
	return array

# print('Array after sorting \n{}'.format(array))

array = create_random_array()
print(array)
print(bubbleSort(array))






