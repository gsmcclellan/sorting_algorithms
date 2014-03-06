"""
	A merge sort recursively splits a list into smaller lists until they
	have a len of one or zero, then combine each list into a single
	sorted list
"""


def merge_sort(nums):

	if len(nums) > 1:
		first_half = nums[:len(nums)//2]
		second_half = nums[len(nums)//2:]

		first_half = merge_sort(first_half)
		second_half = merge_sort(second_half)

		i = j = k = 0
		while i < len(first_half) and j < len(second_half):
			if first_half[i] < second_half[j]:
				nums[k] = first_half[i]
				i += 1
			else:
				nums[k] = second_half[j]
				j += 1
			k += 1
		while i < len(first_half):
			nums[k] = first_half[i]
			k += 1
			i += 1
		while j < len(second_half):
			nums[k] = second_half[j]
			k += 1
			j += 1

		return nums

	else:
		return nums

