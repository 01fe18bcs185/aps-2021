def unset_bit(n, i):
	mask = 1 << i
	mask = ~mask
	return n & mask

print(unset_bit(15, 0))