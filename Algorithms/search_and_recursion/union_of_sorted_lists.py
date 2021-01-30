# Write a function that takes in two sorted lists and outputs a sorted list which is union of two lists

import random
import numpy as np
random.seed(1234)

def create_random_lists(start, end, length):
	return_list=[]
	for i in range(length):
		return_list.append(random.randint(start, end))
	return return_list

# list1 = sorted(create_random_lists(0,100,10))
# list2 = sorted(create_random_lists(50,100, 5))


# # Create sorted union of list1 and list2
def unionSort(left, right):

	union_list=[]

	i=0
	j=0
	while (i<len(left) and (j<len(right))):
		if left[i] < right[j]:
			# print('list1 element at index {}: {}'.format(i, list1[i]))
			# print('list2 element at index {}: {}'.format(j, list2[j]))
			union_list.append(left[i])
			i += 1
		else:
			union_list.append(right[j])
			j += 1

		if i == len(left):
			union_list.extend(right[j:])	
		if j == len(right):
			union_list.extend(left[i:])
        return union_list

# Incase the lists are un sorted pass the lists through merge_sort function
def merge_sort(a):

	if len(a) < 2:
		return a

	middle = len(a)//2
	left = merge_sort(a[:middle])
	right = merge_sort(a[middle:])

	return unionSort(left,right)

unsorted_list1 = create_random_lists(0,1000,100)
unsorted_list2 = create_random_lists(500,1500,100)
# print(unsorted_list1,unsorted_list2)

sorted_list1 = merge_sort(unsorted_list1)
sorted_list2 = merge_sort(unsorted_list2)
# print(sorted_list1, sorted_list2)

union_of_sorted_lists = unionSort(sorted_list1, sorted_list2)
print('Union of sorted lists {}'.format(union_of_sorted_lists))


