# Write a function that takes in three strings and returns a boolean representing whether the third string can be formed by interweaving the first two strings.

def interweavingStrings(one, two, three):
	if len(three) != len(one) + len(two):
		return False
	
	memo = {}
	return DFS(one, two, three, 0, 0, memo)

def DFS(one, two, three, i, j, memo):
	if (i, j) in memo:
		return memo[i, j]
	
	k = i + j
	if k == len(three):
		return True
	
	if i < len(one) and one[i] == three[k]:
		memo[i, j] = DFS(one, two, three, i+1, j, memo)
		if memo[i, j]:
			return True
	if j < len(two) and two[j] == three[k]:
		memo[i, j] = DFS(one, two, three, i, j+1, memo)
		if memo[i, j]:
			return True
			
	memo[i, j] = False
	return False
	

