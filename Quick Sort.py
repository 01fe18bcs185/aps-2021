def quickSort(array):
    QS(array, 0, len(array) - 1)
	return array

def QS(array, start, end):
	if start >= end:
		return
	pivot = start
	left = start + 1
	right = end
	
	while left <= right:
		if array[left] > array[pivot] and array[right] < array[pivot]:
			swap(array, left, right)
		if array[left] <= array[pivot]:
			left += 1
		if array[right] >= array[pivot]:
			right -= 1
	
	swap(array, pivot, right)
	left_subaarray_is_smaller = (right - 1) - start < end - (right + 1)
	if left_subaarray_is_smaller:
		QS(array, start, right - 1)
		QS(array, right + 1, end)
	else:
		QS(array, right + 1, end)
		QS(array, start, right - 1)

def swap(array, i, j):
	array[i], array[j] = array[j], array[i]
	


print(quickSort([1,4,5,2,6]))