# Write a function that takes in two sorted lists and outputs a sorted list which is union of two lists

import random
import numpy as np
random.seed(1234)

def create_random_lists(start, end, length):
	return_list=[]
	for i in range(length):
		return_list.append(random.randint(start, end))
	return return_list

list1 = sorted(create_random_lists(0,100,10))
list2 = sorted(create_random_lists(50,100, 5))


# # Create sorted union of list1 and list2
def unionSort(list1, list2):

	union_list=[]

	i,j=0,0
	while (i<len(list1) and (j<len(list2))):
		if list1[i] < list2[j]:
			print('list1 element at index {}: {}'.format(i, list1[i]))
			print('list2 element at index {}: {}'.format(j, list2[j]))
			union_list.append(list1[i])
			i += 1
		else:
			union_list.append(list2[j])
			j += 1

		if i == len(list1):
			union_list.extend(list2[j:])	
		if j == len(list2):
			union_list.extend(list1[i:])
        return union_list

if __name__ == __main__():
	unionSort(list1, list2)
