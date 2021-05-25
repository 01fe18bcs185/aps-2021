def bubbleSort(nums):
    is_sorted = False
	counter = 0
	
	while not is_sorted:
		is_sorted = True
		for i in range(len(nums) -1 - counter):
			if nums[i] > nums[i + 1]:
				nums[i], nums[i + 1] = nums[i + 1], nums[i]
				is_sorted = False
		counter += 1
	return nums

print(bubbleSort([1,4,5,2,6]))