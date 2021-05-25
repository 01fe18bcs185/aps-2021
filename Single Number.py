# Input: 1, 4, 2, 1, 3, 2, 3
# Output: 4

res = 0
A = [1, 4, 2, 1, 3, 2, 3]

for i in A:
    res ^= i

print(res) 