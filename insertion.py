

"""
	An insertion sort maintains a sorted sublist growing in size by one
	for each pass/iteration. For each number not yet inserted into sublist,
	algorithm iterates backwards through sublist until it finds the
	correct index, shifting each number up in index as it goes
"""

def insertion_sort(nums):
	""" sorts a list of numbers using an insertion sort algorithm """

	# One pass for each number, starting with the second index
	for index in range(1, len(nums) - 1):
		i = index
		current_num = nums[i]
		
		while  i >= 0 and current_num < nums[i-1]:
			nums[i] = nums[i-1]
			i -= 1
		nums[i] = current_num

	return nums 

