'''
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Your goal is to reach the last index in the minimum number of jumps.
You can assume that you can always reach the last index.

Input: nums = [2,3,1,1,4]
Output: 2

'''

def jump(nums):
	if len(nums) <= 1:
		return 0

	max_reach = nums[0]
	next_reach = nums[0]
	jumps = 1

	for i in range(1, len(nums)):
		if max_reach >= len(nums)-1:
		    return jumps
		if i > max_reach:
		    jumps += 1
		    max_reach = next_reach
		next_reach = max(next_reach, nums[i]+i)

	return jumps

print(jump([2,3,1,1,4]))
