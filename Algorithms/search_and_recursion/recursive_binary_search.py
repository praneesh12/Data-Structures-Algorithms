# Recursive binary search

import custom_logger

class search():
	def __init__(self):
		self.log = custom_logger.surgeLogger('surge')


	def recursive_binary(self, array, first, last, element):
		self.log.info('Running recursive_binary_search')

		try:

			if first < last:
				middle = (first+lasting)//2
				if array[middle] == element:
					return 1
				elif array[middle] < element:
					return recursive_binary(array, middle+1, last, element)
				else:
					return recursive_binary(array, first, middle+1, element)
			else:
				return -1

		except Exception:
			self.log.exception('Error running recursive_binary')


array = [1,3,4,8,12,34,44,55,56,76,87,98,122,132,143,156,169,172,188,234]
first = 0
last = len(array)-1
element = 172
search().recursive_binary(array, first, last, element)