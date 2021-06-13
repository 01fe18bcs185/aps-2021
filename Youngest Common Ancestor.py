# Given three inputs, all of which are instances of an AncestralTree class that have an ancestor property pointing to their youngest ancestor The first input is the top ancestor in an ancestral tree (i.e., the only instance that has no ancestor--its ancestor property points to None / null), and the other two inputs are descendants in the ancestral tree. Find Youngest Common Ancestor

#Example
# Input:
# The nodes are from the ancestral tree below.
# topAncestor = node A
# descendantOne = node E
# descendantTwo = node I
#          A
#       /     \
#      B       C
#    /   \   /   \
#   D     E F     G
# /   \
#H     I

# Output:
# node B


class AncestralTree:
    def __init__(self, name):
        self.val = name
        self.ancestor = None


def getYoungestCommonAncestor(A, D1, D2):
	depth1 = get_depth(A, D1)
	depth2 = get_depth(A, D2)
	
	if depth1 > depth2:
		return backtrack(A, D1, D2, depth1 - depth2)
	return backtrack(A, D2, D1, depth2 - depth1)

def get_depth(A, D):
	depth = 0
	while D != A:
		depth += 1
		D = D.ancestor
	return depth

def backtrack(A, lowest, highest, diff):
	while diff > 0:
		lowest = lowest.ancestor
		diff -= 1
	
	while lowest != highest:
		lowest = lowest.ancestor
		highest = highest.ancestor
	
	return lowest

