# Recursive binary search

def recursive_binary_search(array, first, last, element):
	if first < last:
		middle = (first+last)//2
		if array[middle] == element:
			return 1
		elif array[middle] < element:
			return recursive_binary_search(array, middle+1, last, element)
		else:
			return recursive_binary_search(array, first, middle+1, element)
	else:
		return -1


array = [1,3,4,8,12,34,44,55,56,76,87,98,122,132,143,156,169,172,188,234]
first = 0
last = len(array)-1
element = 172
recursive_binary_search(array, first, last, element)