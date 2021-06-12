# Write a function that takes in a Binary Tree and returns its diameter. The diameter of a binary tree is defined as the length of its longest path, even if that path doesn't pass through the root of the tree.

def binaryTreeDiameter(root):
	res = 0
	
	def dfs(node):
		nonlocal res
		if not node:
			return 0
		
		left = dfs(node.left)
		right = dfs(node.right)
		res = max(res, left + right)
		
		return max(left, right) + 1
	
	dfs(root)
	return res

