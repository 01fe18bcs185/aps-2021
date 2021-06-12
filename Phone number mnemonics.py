# Given a string containing digits from 0-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

def phoneNumberMnemonics(nums):
	def dfs(nums, cur):
		if not nums:
			res.append("".join(cur))
			return 

		for char in d[nums[0]]:
			dfs(nums[1:], cur+[char])
		

	d = {"1":"1", "2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz", "0":"0"}
	res = []
	dfs(nums, [])
	return res
