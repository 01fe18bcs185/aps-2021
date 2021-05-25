def assign(N, cost):
	dp = [float('inf')] * (2 ** N)
	dp[0] = 0

	for i in range(2 ** N):
		x = bin(i).count('1')
		for j in range(N):
			mask = 1 << j
			if not (i & mask):
				dp[i|(1<<j)] = min(dp[i|(1<<j)], dp[i]+cost[x][j])

	return dp[-1]

cost = [[3,2,7], [5,1,3], [2,7,2]]
N = 3

print(assign(N, cost))
