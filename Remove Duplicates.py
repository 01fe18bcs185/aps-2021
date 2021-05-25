# Input: [3, 2, 3, 6, 3, 10, 9, 3], Key=3
# Output: 4
# Explanation: The first four elements after removing every 'Key' will be [2, 6, 10, 9].

nums = [3, 2, 3, 6, 3, 10, 9, 3]
k = 3

i = j = 0

for j in range(len(nums)):
	if nums[j] != k:
		nums[i] = nums[j]
		i += 1

print(nums)
