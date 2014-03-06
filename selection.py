

""" 
	A selection sort is similar to a bubble sort. It makes multiple
	passes through the list. Where it differs, however is that a 
	selection sort will only switch one number per pass.
"""

def selection_sort(nums):
	"""Takes a list of numbers, and sorts them using a selection sort algorithm"""

	# Determine number of passes
	for pass_limit in range(len(nums)-1, 0, -1):

		max_val_location = 0
		# Make pass for each iteration
		for i in range(1, pass_limit):
			if nums[i] > nums[max_val_location]:
				max_val_location = i

		# Swap largest number with the highest index
		nums[max_val_location], nums[pass_limit] = nums[pass_limit], nums[max_val_location]

	return nums