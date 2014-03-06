


"""
	A shell sort is an improved version of the insertion sort where where
	break our list into sublists that will each be sorted using the
	insertion sort. We then increase the number of sublists until we are
	doing a normal insertion sort
"""

[1, 6, 9, 10, 99, 4, 201, 5, 12]


def shell_sort(nums):
	""" Sorts a list of numbers using a shell sort algorithm """

	# For each iteration, double the size of each sublist / halve the number of sublists
	num_sublists = len(nums) // 2

	while(num_sublists) > 0:
		gap = num_sublists

		# Iterate once for each sublist
		for start_index in range(num_sublists):

			# Perform a gap insertion sort for each iteration
			for current_index in range(start_index + gap, len(nums)-1, gap):
				current_num = nums[current_index]

				while current_index > 0 and current_num < nums[current_index - gap]:
					nums[current_index] = nums[current_index - gap]
					current_index -= gap
				nums[current_index] = current_num

		num_sublists = num_sublists // 2
	return nums



