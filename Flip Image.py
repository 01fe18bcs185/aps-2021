# Given a binary matrix representing an image, we want to flip the image horizontally, then invert it.

# To flip an image horizontally means that each row of the image is reversed. For example, flipping [0, 1, 1] horizontally results in [1, 1, 0].

# To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. For example, inverting [1, 1, 0] results in [0, 0, 1].

# Example 1:

# Input: [
#  [1,0,1],
#  [1,1,1],
#  [0,1,1]
#]
#Output: [
#  [0,1,0],
#  [0,0,0],
#  [0,0,1]
#]

def solve(matrix):
	length = len(matrix)

	for row in matrix:
		for i in range((length+1)//2):
		    row[i], row[length-i-1] = row[length-i-1]^1, row[i]^1
	
	return matrix

