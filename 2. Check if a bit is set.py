def check_set_bit(n, i):
	mask = 1 << i
	return True if n & mask else False

print(check_set_bit(3, 2))