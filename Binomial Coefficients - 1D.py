def binomial_coef(n, k):
	dp = [0 for _ in range(k+1)]
	dp[0] = 1

	for i in range(1, n + 1):
		for j in range(1, min(i, k) + 1)[::-1]:
			dp[j] = dp[j] + dp[j-1]

	return dp[k]
	
print(binomial_coef(4, 2))