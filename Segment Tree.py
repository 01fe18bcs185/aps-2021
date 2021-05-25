class SegmentTree:
	def __init__(self, nums):
		self.l = len(nums)
		self.tree = [0]*self.l + nums
		for i in range(self.l - 1, 0, -1):
			self.tree[i] = self.tree[i<<1] + self.tree[i<<1|1]
	
	def update(self, i, val):
		i = self.l + i
		self.tree[i] = val
        
		while i > 1:
			self.tree[i>>1] = self.tree[i] + self.tree[i^1]
			i >>= 1
		
	def sumRange(self, i, j):
		m = self.l + i
		n = self.l + j
		res = 0
		while m <= n:
			if m & 1:
				res += self.tree[m]
				m += 1
			if n & 1 == 0:
				res += self.tree[n]
				n -= 1
			m >>= 1
			n >>= 1
		return res

s = SegmentTree([1,2,3,4,5])
print(s.sumRange(1,3))
s.update(3,0)
print(s.sumRange(1,3))