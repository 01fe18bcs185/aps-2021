# Input: "abdbca"
# Output: 3
# Explanation: LPS is "bdb".

from collections import defaultdict as dd

def solve(s):
	n = len(s)
	if not s:
		return 0

	dp = dd(lambda :False)

	for i in range(n):
		dp[i, i] = True
	res = 1

	for i in range(n)[::-1]:
		for j in range(i+1, n):
			if s[i] == s[j] and (dp[i+1, j-1] or j-i == 1):
				dp[i, j] = True
				res = max(res, j-i+1)

	return res

s = "abdbca"
print(solve(s))