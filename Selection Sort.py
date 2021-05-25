def selectionSort(array):
    cur_idx = 0
	while cur_idx < len(array):
		small_idx = cur_idx
		for i in range(cur_idx + 1, len(array)):
			if array[small_idx] > array[i]:
				small_idx = i
		array[cur_idx], array[small_idx] = array[small_idx], array[cur_idx]
		cur_idx += 1
	return array

print(selectionSort([1,4,5,2,6]))