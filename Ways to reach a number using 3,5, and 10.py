# Input: n = 13
# Output: 2
# There are following 2 ways to reach 13
# (3, 5, 5)
# (3, 10)

def solve(n):
	dp = [1] + [0]*n

	for i in (3,5,10):
		for j in range(1, n+1):
			if j >= i:
				dp[j] += dp[j-i]

	return dp[-1]


n = 13
print(solve(n))