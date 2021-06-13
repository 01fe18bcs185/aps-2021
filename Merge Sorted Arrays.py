# Write a function that takes in a non-empty list of non-empty sorted arrays of integers and returns a merged list of all of those arrays.

# The integers in the merged list should be in sorted order.

# Example
# Input: 
# arrays = [
#  [1, 5, 9, 21],
#  [-1, 0],
#  [-124, 81, 121],
#  [3, 6, 12, 20, 150],
#]

# Output:
# [-124, -1, 0, 1, 3, 5, 6, 9, 12, 20, 21, 81, 121, 150]

from heapq import heappush, heappop
def mergeSortedArrays(nums):
    res = []
	pq = []
	
	for num in nums:
		heappush(pq, [num[0], 0, num])
	
	while pq:
		n, i, num = heappop(pq)
		res.append(n)
		
		if i < len(num) - 1:
			heappush(pq, [num[i+1], i+1, num])
	return res
