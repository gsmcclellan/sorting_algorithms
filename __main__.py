# Std Lib
import sys
import os
from random import randint

# Add this module to path
path = os.path.dirname(sys.modules[__name__].__file__)
path = os.path.join(path, '..')
sys.path.insert(0, path)

# Import sort functions
from sort import *


def main(*argv):
	try:
		list_size = int(argv[0])
	except:
		list_size = 1000

	try:
		max_num_size = int(argv[1])
	except:
		max_num_size = 10000

	list_to_sort = [randint(1, 200) for x in range(list_size)]
	
	assert bubble(list_to_sort) == short_bubble(list_to_sort) == selection(list_to_sort) == insertion(list_to_sort) == shell(list_to_sort) \
		== merge(list_to_sort) == quick(list_to_sort)


if __name__ == "__main__":
	main(*sys.argv[1:])