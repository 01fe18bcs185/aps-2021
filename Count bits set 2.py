def count_bits_set2(n):
	count = 0
	while n:
		n = n & (n-1)
		count += 1
	return count

print(count_bits_set2(14))