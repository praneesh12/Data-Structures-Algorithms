#myLib.py

import logging
import myApp

def do_something(n,m):
	try:
		return (n/m)
	except Exception as e:
		logging.debug('Error message'.format(e))

if __name__ == "__main__":
	print(do_something(n=3,m=0))
