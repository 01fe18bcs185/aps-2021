def binarySearch(nums, target):
    l = 0
	r = len(nums) - 1
	
	while l <= r:
		mid = (l + r) // 2
		if nums[mid] == target:
			return mid
		if nums[mid] < target:
			l = mid + 1
		else:
			r = mid - 1
	return -1

# nums = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
# target = 33
print(binarySearch(nums, target)
# output: 3
