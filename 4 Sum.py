# Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. The function should find all quadruplets in the array that sum up to the target sum and return a two-dimensional array of all these quadruplets in no particular order.

# Example
# Input: array = [7, 6, 4, -1, 1, 2] targetSum = 16
# Output: [[7, 6, 4, -1], [7, 6, 1, 2]]

def fourNumberSum(nums, targetSum):
	nums.sort()
	res = []
	for i in range(len(nums)-3):
		if i > 0 and nums[i-1] == nums[i]:
			continue
		for j in range(i + 1, len(nums) - 2):
			if j > i + 1 and nums[j-1] == nums[j]:
				continue
			
			l = j + 1
			r = len(nums) - 1
			target = targetSum - nums[i] - nums[j]
			
			while l < r:
				cur_sum = nums[l] + nums[r]
				if cur_sum == target:
					res.append([nums[i], nums[j], nums[l], nums[r]])
					l += 1
					r -= 1
					while l < r and nums[l] == nums[l - 1]:
						l += 1
					while l < r and nums[r] == nums[r + 1]:
						r -= 1
				elif cur_sum < target:
					l += 1
				else:
					r -= 1
	return res
