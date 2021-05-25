# Input: {4,2,3,6,10,1,12}
# Output: 5
# Explanation: The LIS is {2,3,6,10,12}.

def solve(nums):
	if not nums:
		return 0
	n = len(nums)
	dp = [1] * n

	for i in range(1, len(dp)):
		cur = nums[i]
		for j in range(i):
			prev = nums[j]
			if prev < cur and dp[i] <= dp[j] + 1:
				dp[i] = dp[j] + 1

	return max(dp)

nums = [4,2,3,6,10,1,12]
print(solve(nums))