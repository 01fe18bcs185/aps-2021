# The distance between a node in a Binary Tree and the tree's root is called the node's depth.

# Write a function that takes in a Binary Tree and returns the sum of its nodes' depths.

def nodeDepths(node, depth = 0):
    if not node:
		return 0
	return depth + nodeDepths(node.left, depth + 1) + nodeDepths(node.right, depth + 1)
