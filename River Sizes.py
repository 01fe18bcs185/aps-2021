# You're given a two-dimensional array (a matrix) of potentially unequal height and width containing only 0s and 1s. Each 0 represents land, and each 1 represents part of a river. A river consists of any number of 1s that are either horizontally or vertically adjacent (but not diagonally adjacent). The number of adjacent 1s forming a river determine its size.

# Write a function that returns an array of the sizes of all rivers represented in the input matrix. The sizes don't need to be in any particular order.

# Example:
# Input
# matrix = [
#   [1, 0, 0, 1, 0],
#   [1, 0, 1, 0, 0],
#   [0, 0, 1, 0, 1],
#   [1, 0, 1, 0, 1],
#   [1, 0, 1, 1, 0],
# ]
# Sample Output
# [1, 2, 2, 2, 5] // The numbers could be ordered differently.

# // The rivers can be clearly seen here:
# // [
# //   [1,  ,  , 1,  ],
# //   [1,  , 1,  ,  ],
# //   [ ,  , 1,  , 1],
# //   [1,  , 1,  , 1],
# //   [1,  , 1, 1,  ],
# // ]

def riverSizes(matrix):
    if not matrix:
		return [0]
	res = []
	
	r = len(matrix)
	c = len(matrix[0])
	
	for i in range(r):
		for j in range(c):
			if matrix[i][j] == 1:
				count = [0]
				dfs(matrix, i, j, r, c, count)
				res.append(count[0])
	return res

def dfs(matrix, i, j, R, C, count):
	if i < 0 or j < 0 or i >= R or j >= C or matrix[i][j] == 0:
		return
	
	count[0] += 1
	matrix[i][j] = 0
	
	dfs(matrix, i + 1, j, R, C, count)
	dfs(matrix, i, j + 1, R, C, count)
	dfs(matrix, i - 1, j, R, C, count)
	dfs(matrix, i, j - 1, R, C, count)

