import logging
import os, sys

try:
    user_paths = os.environ['PYTHONPATH'].split(os.pathsep)
except KeyError:
    user_paths = []
print(user_paths)
import binary_search


logging.basicConfig(filename='myapp.log', level=logging.INFO)
logging.info('Started')
binary_search.binary_search_iterative(input_array=[1,2,3,4,5,7,8,9,12,22,34,36], value=20)
logging.info('Finished')
