# Write a function that returns true if this Binary Tree is height balanced and false if it isn't.

# A Binary Tree is height balanced if for each node in the tree, the difference between the height of its left subtree and the height of its right subtree is at most 1.

def dfs(node):
	if not node:
		return 1
	left_height = dfs(node.left)
	right_height = dfs(node.right)
	return max(left_height, right_height) + 1
		
def heightBalancedBinaryTree(node):
    if not node:
		return True
	lh = dfs(node.right)
	rh = dfs(node.left)
	
	if abs(lh-rh) > 1:
		return False
	
	return heightBalancedBinaryTree(node.left) and heightBalancedBinaryTree(node.right)
	
