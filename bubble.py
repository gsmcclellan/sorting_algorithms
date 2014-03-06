# Std Lib
from random import randint
import sys
import time


"""
	A bubble sort makes multiple passes, iterating through and comparing
	each adjacent pair of numbers, each time placing the larger number 
	at the higher index.
"""


def bubble_sort(nums):
	""" Applies a bubble sort to the given list, returns sorted list"""

	# Determine number of passes to make for bubble sort
	for pass_limit in range(len(nums)-1, 0, -1):

		# make sorting pass for each one
		for i in range(0, pass_limit):

			# For each pair, if lower index is larger, swap the pair
			if nums[i] > nums[i+1]:
				nums[i], nums[i+1] = nums[i+1], nums[i]

	return nums


def short_bubble_sort(nums):
	""" Cuts a bubble sort short if there are no exchanges during a any given pass """

	# Determine max number of passes we will need to make
	pass_limit = len(nums) - 1
	finished = False

	# Keep making sorting passes until no exchanges are made
	while pass_limit >= 0 and not finished:
		finished = True

		# Make sorting pass
		for i in range(0, pass_limit):

			# For each pair, if lower index is larger, swap the pair
			if nums[i] > nums[i+1]:
				nums[i], nums[i+1] = nums[i+1], nums[i]
				# Exchange is made, sorting is not finished
				finished = False

	return nums
