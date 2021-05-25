# Denominations: {1,2,3}
# Total amount: 5
# Output: 2
# Explanation: We need minimum of two coins {2,3} to make a total of '5'

def ubknapsack(nums, target):
	n = len(nums)

	dp = [[float('inf') for _ in range(target + 1)] for _ in range(n)]

	for i in range(n):
		dp[i][0] = 0

	for j in range(1, target + 1):
		if j >= nums[i]:
			dp[i][j] = dp[i][j-nums[i]] + 1

	for i in range(n):
		for j in range(1, target + 1):
			dp[i][j] = min(dp[i-1][j], dp[i][j-nums[i]] + 1)

	return dp[-1][-1]

nums = [1,2,3]
target = 5
print(ubknapsack(nums, target))