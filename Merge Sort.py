def mergeSort(array):
    if len(array) <= 1:
		return array
	auxiliary_array = array[:]
	MS(array, 0, len(array) - 1, auxiliary_array)
	return array

def MS(array, start_idx, end_idx, auxiliary_array):
	if start_idx == end_idx:
		return
	middle_idx = (start_idx + end_idx) // 2
	MS(auxiliary_array, start_idx, middle_idx, array)
	MS(auxiliary_array, middle_idx + 1, end_idx, array)
	do_merge(array, start_idx, middle_idx, end_idx, auxiliary_array)

def do_merge(array, start_idx, middle_idx, end_idx, auxiliary_array):
	k = start_idx
	i = start_idx
	j = middle_idx + 1
	
	while i <= middle_idx and j <= end_idx:
		if auxiliary_array[i] <= auxiliary_array[j]:
			array[k] = auxiliary_array[i]
			i += 1
		else:
			array[k] = auxiliary_array[j]
			j += 1
			
		k += 1
	
	while i <= middle_idx:
		array[k] = auxiliary_array[i]
		i += 1
		k += 1
	while j <= end_idx:
		array[k] = auxiliary_array[j]
		j += 1
		k += 1

print(mergeSort([1,4,5,2,6]))