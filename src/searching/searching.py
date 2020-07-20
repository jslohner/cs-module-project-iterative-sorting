def linear_search(arr, target):
	for i in range(0, len(arr)):
		if arr[i] == target:
			return i
	return -1   # not found

# Write an iterative implementation of Binary Search
def binary_search(arr, target):
	low = 0
	high = len(arr) - 1
	while low <= high:
		mid = (low + high) // 2
		if arr[mid] == target:
			return mid
		elif target < arr[mid]:
			high = mid - 1
		elif target > arr[mid]:
			low = mid + 1
	return -1  # not found
