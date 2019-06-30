#myLib.py

import logging
import os
import sys

def surgeLogger(name='surge', loglevel='INFO'):
    logger = logging.getLogger(name)
    print(logger)
    
    # if logger 'name' already exists, return it to avoid logging duplicate
    if logger.handlers:
    	return logger
    # if logger 'name' does not already exist, create it and attach handlers
    else :
    	# set logLevel to loglevel or to INFO if requested level is incorrect
	    loglevel = getattr(logging, loglevel.upper(), logging.INFO)
	    logger.setLevel(loglevel)
	    fmt = '%(asctime)s %(filename)-10s%(levelname)-8s:%(name)s: %(message)s'
	    fmt_date = '%Y-%m-%d T%T%Z'
	    formatter = logging.Formatter(fmt, fmt_date)

	    # Print messages on console
	    stream_handler = logging.StreamHandler()
	    stream_handler.setFormatter(formatter)
	    logger.addHandler(stream_handler)

	    # Save messages in the file
	    file_handler = logging.FileHandler('./surge.log')
	    file_handler.setFormatter(formatter)
	    logger.addHandler(file_handler)

    if logger.name == 'surge':
    	logger.warning('Running: %s %s', os.path.basename(sys.argv[0]), ' '.join(sys.argv[1:]))

    return logger

if __name__=='__main__':
    surgeLogger()



# def surgeLogger():
# 	logger = logging.getLogger(__name__)
# 	logger.setLevel(logging.DEBUG)

# 	formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

# 	file_handler = logging.FileHandler('sample.log')
# 	file_handler.setLevel(logging.ERROR)
# 	file_handler.setFormatter(formatter)

# 	stream_handler = logging.StreamHandler()
# 	stream_handler.setFormatter(formatter)

# 	logger.addHandler(file_handler)
# 	logger.addHandler(stream_handler)

