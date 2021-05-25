# Input: [3, 1, 5, 12, 2, 11], K = 3
# Output: [5, 12, 11]

from heapq import heappush, heappop

nums = [3, 1, 5, 12, 2, 11]
k = 3
pq = []

for num in nums:
    heappush(pq,num)

    if len(pq) > k:
        heappop(pq)

print(pq)