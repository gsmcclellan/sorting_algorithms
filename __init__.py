# Std Lib
import time

# sort imports
from bubble import bubble_sort, short_bubble_sort
from selection import selection_sort
from insertion import insertion_sort
from shell import shell_sort
from merge import merge_sort
from quick import quick_sort


def print_time(function):

	def wrapper(*args):
		"""Wrapper calculates time taken by each function, prints result, then returns sorted list as normal."""

		time_before = time.clock()
		result = function(*args)
		time_after = time.clock()

		print "{func_name} sort sorted {length} items in {time} seconds".format(
			func_name=function.func_name, 
			length=len(result), 
			time=(time_after - time_before)
		)

		return result

	return wrapper


@print_time
def bubble(*args):
	return bubble_sort(*args)


@print_time
def short_bubble(*args):
	return short_bubble_sort(*args)


@print_time
def selection(*args):
	return selection_sort(*args)


@print_time
def insertion(*args):
	return insertion_sort(*args)


@print_time
def shell(*args):
	return shell_sort(*args)


@print_time
def merge(*args):
	return merge_sort(*args)


@print_time
def quick(*args):
	return quick_sort(*args)

