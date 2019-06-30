# Sorting Algorithm Naive approach : Bubble Sort

#Create a randomized array of length 'length' and range 0,maxint
from random import randint
import logging
import os


logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))

def create_random_array(length=10, maxint=50):
	try :
		return [randint(0, maxint) for _ in range(length)]
	except Exception:
		myLib.INFO('Random numbers are {}'.format())

def bubbleSort(array):
	swapped=True
	while swapped:
		swapped=False
		for i in range(1,len(array)):
			if array[i-1] > array[i]:
				array[i],array[i-1] = array[i-1],array[i]
				swapped=True
	return array
