# Write a function that takes in an array of unique integers and returns an array of all permutations of those integers in no particular order.

# If the input array is empty, the function should return an empty array.

def getPermutations(nums):
    res = []
	_helper(nums, [], res)
	return res

def _helper(nums, cur, res):
	if not nums and cur:
		res.append(cur)
		return
	
	for i in range(len(nums)):
		new_cur = cur + [nums[i]]
		new_nums = nums[:i] + nums[i+1:]
		_helper(new_nums, new_cur, res)
