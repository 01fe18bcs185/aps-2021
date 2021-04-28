def set_bit(n, i):
	mask = 1 << i
	return n | mask

print(set_bit(3, 0))