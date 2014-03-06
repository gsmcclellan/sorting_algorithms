

"""
	A quicksort uses a similar recursive divide and conquer strategy to
	the one used by merge sort. It begins by picking a pivot point, then
	a left end and a right end. Increment the left end until you have a
	number bigger than the pivot point number, and decrement the right end
	until you have a number smaller. Then swap the two and continue on until
	the left end > right end.
"""

def quick_sort(nums):
	""" Sorts a list of numbers using a quick sort algorithm """

	if len(nums) <= 1:
		return nums

	# Pivot point is first index
	pivot = 0
	left_end = 1
	right_end = len(nums) - 1

	# Go until left_end and right_end meet or cross
	while left_end < right_end:

		# Increment left_end until it is greater than pivot
		while nums[left_end] < nums[pivot]:
			left_end += 1

		# Decrement right_end until it is less than pivot
		while nums[right_end] > nums[pivot]:
			right_end -= 1

		# Swap the two and increment/decrement
		nums[left_end], nums[right_end] = nums[right_end], nums[left_end]
		left_end += 1
		right_end -= 1

	# If right end is greater than pivot, list is sorted
	if nums[right_end] > nums[pivot]:
		# Right end becomes new pivot
		nums[pivot], nums[right_end], pivot = nums[right_end], nums[pivot], right_end
		return quick_sort(nums[:pivot]) + quick_sort(nums[pivot:])
	else:
		return nums

