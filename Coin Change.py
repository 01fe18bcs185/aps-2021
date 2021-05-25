# Denominations: {1,2,3}
# Total amount: 5
# Output: 5
# Explanation: There are five ways to make the change for '5', here are those ways:
#   1. {1,1,1,1,1} 
#   2. {1,1,1,2} 
#   3. {1,2,2}
#   4. {1,1,3}
#   5. {2,3}

def ubknapsack(nums, target):
	n = len(nums)

	dp = [[0 for _ in range(target + 1)] for _ in range(n)]

	for i in range(n):
		dp[i][0] = 1

	for i in range(n):
		for j in range(1, target + 1):
			if i >= 1:
				dp[i][j] = dp[i-1][j]
			if j >= nums[i]:
				dp[i][j] += dp[i][j-nums[i]]

	return dp[-1][-1]

nums = [1,2,3]
target = 5
print(ubknapsack(nums, target))