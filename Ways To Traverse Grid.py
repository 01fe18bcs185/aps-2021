# Given two positive integers representing the width and height of a grid-shaped, rectangular graph. Write a function that returns the number of ways to reach the bottom right corner of the graph when starting at the top left corner. Each move you take must either go down or right. In other words, you can never move up or left in the graph.

def numberOfWaysToTraverseGraph(C, R):
    M = [[0 for _ in range(C+1)] for _ in range(R+1)]
	
	for i in range(1, C+1):
		for j in range(1, R+1):
			if i == 1 or j == 1:
				M[j][i] = 1
			else:
				M[j][i] = M[j][i-1] + M[j-1][i]
	
	return d[R][C]
	
	
