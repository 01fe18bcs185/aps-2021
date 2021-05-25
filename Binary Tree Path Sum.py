#Given a binary tree and a number N, find if the tree has a path from root-to-leaf such that the sum of all the node values of that path equals N.

class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

root = a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)
g = TreeNode(7)

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g

from collections import deque

def has_path(node,s):
    if not node:
        return False
    if node.val == s and node.left == None and node.right == None:
        return True
    return has_path(node.left,s-node.val) or has_path(node.right, s-node.val)

print(has_path(root,12)) 
