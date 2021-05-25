# Input: s1 = "abdca"
#        s2 = "cbda"
# Output: 3
# Explanation: The longest common subsequence is "bda".

from collections import defaultdict as dd

def solve(s, t):
	if not s or not t:
		return 0

	dp = dd(int)
	m = len(s) + 1
	n = len(t) + 1

	for i in range(1, m):
		for j in range(1, n):
			if s[i-1] == t[j-1]:
				dp[i, j] = 1 + dp[i-1, j-1]
			else:
				dp[i, j] = max(dp[i-1, j], dp[i, j-1])

	return dp[m-1, n-1]

s = "abdca"
t = "cbda"
print(solve(s, t))