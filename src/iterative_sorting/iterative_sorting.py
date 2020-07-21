# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
	# loop through n-1 elements
	for i in range(0, len(arr) - 1):
		cur_index = i
		smallest_index = cur_index
		# TO-DO: find next smallest element
		# (hint, can do in 3 loc)
		# loop through elements right of current
		for n in range((cur_index + 1), (len(arr))):
			# if num is less than smallest
			# change smalles index to n
			if arr[n] < arr[smallest_index]:
				smallest_index = n
		# TO-DO: swap
		# swap current num with smallest num
		arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]
	return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
	# my original solution
	# loop through length of array but in descending order
	for range_num in range((len(arr) - 1), 0, -1):
		# loop through part of array
		# which hasn't been swapped
		for i in range(0, range_num):
			# if current num is greater
			# than the next swap them
			if arr[i] > arr[i + 1]:
				arr[i], arr[i + 1] = arr[i + 1], arr[i]
	return arr

	# while loop solution
	# sort = True
	# while sort:
	# 	sort = False
	# 	for i in range(0, len(arr) - 1):
	# 		if arr[i] > arr[i + 1]:
	# 			arr[i], arr[i + 1] = arr[i + 1], arr[i]
	# 			sort = True
	# return arr

# recursive solution
# def bubble_sort(arr, length):
# 	for i in range(0, length):
# 		if arr[i] > arr[i + 1]:
# 			arr[i], arr[i + 1] = arr[i + 1], arr[i]
# 	if length > 0:
# 		arr = bubble_sort(arr, length - 1)
# 	return arr
'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the
buckets.

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, max=0):
	for num in arr:
		if num > max:
			max = num
	buckets = [0 for i in range(max + 1)]
	sorted = []
	for num in arr:
		if num < 0:
			return 'Error, negative numbers not allowed in Count Sort'
	for num in arr:
		buckets[num] += 1
	for i in range(0, len(buckets)):
		sorted.extend([i] * buckets[i])
	# for i in range(0, len(arr)):
	# 	arr[i] = sorted[i]
	return sorted
