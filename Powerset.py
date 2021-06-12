# Write a function that takes in an array of unique integers and returns its powerset.

# The powerset P(X) of a set X is the set of all subsets of X. For example, the powerset of [1,2] is [[], [1], [2], [1,2]].

def powerset(array):
	subset = [[]]
	
	for num in array:
		for i in range(len(subset)):
			s = subset[i]
			subset.append(s + [num])
	
	return subset

