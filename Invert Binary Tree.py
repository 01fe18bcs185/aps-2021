# Write a function that takes in a Binary Tree and inverts it. In other words, the function should swap every left node in the tree for its corresponding right node.

def _helper(node):
	if not node:
		return
	node.left, node.right = node.right, node.left
	_helper(node.left)
	_helper(node.right)

def invertBinaryTree(tree):
	_helper(tree)
	return tree
