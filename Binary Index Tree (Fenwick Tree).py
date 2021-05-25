class FenwickTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.a = nums
        self.BIT = [0] * (self.n + 1)
        
        for i, e in enumerate(nums):
            self.insert(i, e)
                
    def insert(self, i, val):
        i += 1
        while i <= self.n:
            self.BIT[i] += val
            i += (i & -i)
                
    def update(self, i, val):
        diff = val - self.a[i]
        self.a[i] = val
        self.insert(i, diff)

    def sumRange(self, i, j):
        res, j = 0, j + 1
        while j:
            res += self.BIT[j]
            j -= (j & -j)
        while i:
            res -= self.BIT[i]
            i -= (i & -i)
        return res

b = FenwickTree([1,2,3,4,5])
print(b.sumRange(1,3))
b.update(3,0)
print(b.sumRange(1,3))
