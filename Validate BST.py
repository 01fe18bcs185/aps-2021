# Write a function that takes in a potentially invalid Binary Search Tree (BST) and returns a boolean representing whether the BST is valid.

def validateBst(tree):
	return _helper(tree, float("-inf"), float("inf"))

def _helper(node, m, M):
	if node is None:
		return True
	if node.value < m or node.value >= M:
		return False
	left_valid = _helper(node.left, m, node.value)
	right_valid = _helper(node.right, node.value, M)
	return left_valid and right_valid

