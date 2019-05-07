# Merge Sort
from random import randint
def create_random_array(length=10, maxint=50):
	return [randint(0, maxint) for _ in range(length)]

new_array = create_random_array(length=3, maxint=50)
print(new_array)

# class sorting():
# 	def __init__(algorith_name = None, array_length=10, randomized=True):
# 		self.algorith_name = algorith_name
# 		self.array_length = array_length


def divide_array(array):
	left_idx = 0
	right_idx = len(array)-1

	middle_idx = (left_idx + right_idx)//2
	left_array = array[0:middle_idx]
	right_array = array[middle_idx:]

	return left_array, right_array

def mergeSort(array):
	merged_array = []
	idx = 0
	# first = 0
	# last = len(array)-1
	if len(array)==0 or len(array)==1:
		return array
	else:
		left_array, right_array = divide_array(array)
		while idx < len(left_array) or idx < len(left_array):
			if left_array[idx] < right_array[idx]:
				merged_array.append(left_array[idx])
			else:
				merged_array.append(right_array[idx])
			idx += 1
	return merged_array
		


print(mergeSort(new_array))



# def mergeSort(array):
# 	# Step1: Break array into n subarrays where n is the length of the original array
# 	# Each array is a sorted list
# 	temp_array = ([[arr] for arr in array])

# 	#Step2:Recursively compare array elements and merge them together till sorted array of length n is formed
# 	# Recursion base case: 
# 	swapped = True
# 	merged_array = []
# 	while swapped:
# 		swapped=False
# 		for i in range(len(temp_array)-1):
# 			if array[i+1] < array[i]:
# 				array[i],array[i+1] = array[i+1],array[i]
# 				swapped=True

# 	return array

# new_array = create_random_array(length=10, maxint=50)
# print('Randomized unsorted array \n{}'.format(new_array))
# print(mergeSort(new_array))












