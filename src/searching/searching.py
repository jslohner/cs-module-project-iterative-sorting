def linear_search(arr, target):
	# loop through indices of array
	for i in range(0, len(arr)):
		# if current element matches target
		# return index of currrent element
		if arr[i] == target:
			return i
	return -1   # not found

# Write an iterative implementation of Binary Search
def binary_search(arr, target):
	# define low point and high point
	low = 0
	high = len(arr) - 1
	# while low point <= high continue looping
	while low <= high:
		# mid point is low and high points
		# added together and divided by 2
		mid = (low + high) // 2
		# if mid point matches target
		# return mid index
		if arr[mid] == target:
			return mid
		# if target < mid change high point
		# to 1 below mid which has been checked
		elif target < arr[mid]:
			high = mid - 1
		# if target > mid change low point
		# to 1 above mid which has been checked
		elif target > arr[mid]:
			low = mid + 1
	return -1  # not found
