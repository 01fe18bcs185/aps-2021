# Given the root node of a Binary Tree, a target value of a node that's contained in the tree, and a positive integer k. Write a function that returns the values of all the nodes that are exactly distance k from the node with target value.

from collections import deque
def findNodesDistanceK(root, target, k):
    def findTarget(node):
		if node:
			if node.value == target:
				return node
			return findTarget(node.left) or findTarget(node.right)
	
	def dfs(node, par = None):
		if node:
			node.par = par
			dfs(node.left, node)
			dfs(node.right, node)
	
	def bfs(target):
		seen = set()
		q = deque()
		q.append((0, target))
		seen.add(target)
		res = []
		
		while q:
			dist, node = q.popleft()
			if dist == k:
				res.append(node.value)
			for nei in node.par, node.left, node.right:
				if nei and nei not in seen:
					seen.add(nei)
					q.append((dist+1, nei))
		
		return res
	
	targetNode = findTarget(root)
	dfs(root)
	return bfs(targetNode)
