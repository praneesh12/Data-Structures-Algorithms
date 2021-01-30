#linear search

def linear_search(search_list, search_element):
	return_index = None
	for i in search_list:
		if i == search_element:
			print("Search element is at index {}".format(search_list.index(i)))
			return search_list.index(i)
	return -1
	print("Search element not present in the list")

linear_search(search_list=[1,2,3,4,5,6,7,8,9,10], search_element=8)