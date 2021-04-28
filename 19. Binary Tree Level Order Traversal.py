class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

root = TreeNode(12)
a = TreeNode(7)
b = TreeNode(1)
c = TreeNode(3)
d = TreeNode(9)
e = TreeNode(10)
f = TreeNode(5)

root.left = a
root.left.left = d
root.right = b
root.right.right = f
root.right.left = e

##########################################
from collections import deque
def traverse(node,res):
    if not node:
        return
    queue = deque()
    queue.append(root)

    while queue:
        cur_level = []
        level_size = len(queue)

        for _ in range(level_size):
            current_node = queue.popleft()
            cur_level.append(current_node.val)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

        res.append(cur_level)
    return res

res = []
traverse(root,res)
print(res)
