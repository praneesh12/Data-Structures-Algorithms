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


def merge(left_array, right_array):
	merged_array = []
	i = 0
	j=0
	while (i < len(left_array)) and (j < len(left_array)):
		if left_array[i] < right_array[j]:
			merged_array.append(left_array[i])
			i =+ 1
		else:
			merged_array.append(right_array[j])
			j += 1
	while (i < len(left_array)):
		merged_array.append(left_array[i])
		i += 1
	while (j < len(right_array)):
		merged_array.append(right_array[j])
		j += 1

	return merged_array

def merge_sort(array):

	if len(array) < 2:
		return array
	else:
		middle = len(array)//2
		left_array = merge_sort(array[:middle])
		print(left_array)
		right_array = merge_sort(array[middle:])
		print(right_array)
		return merge(left_array, right_array)

print(merge_sort(new_array))