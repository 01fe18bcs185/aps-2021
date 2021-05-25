def binomial_coef(n, k):
	if k == 0 or k == n:
		return 1
	return binomial_coef(n-1, k-1) + binomial_coef(n-1, k)

print(binomial_coef(4, 2))