# Quick Sort 

from random import randint

def create_array(size=4, max=50):
	return [randint(0, size) for _ in range(size)]

# Create a function which sorts an array using QuickSort techniqu, pivot position should be randomized

def quickSort(array):
	if len(array)<=1:
		return array
		
	#Create list which will have smaller, larger and pivot elements
	smaller = []
	larger = []
	equal = []
	pivot = array[randint(0, len(array)-1)]
	print(pivot)
	

	for x in array:
		if x<pivot:
			smaller.append(x)
		elif x==pivot:
			equal.append(x)
		else:
			larger.append(x)

	return quickSort(smaller)+equal+quickSort(larger)

a = create_array()
print('Unsorted array:', a)
s=quickSort(a)
print('Sorted array :',s)