# Given the root of a binary tree, return the inorder traversal of its nodes' values.

 def inorderTraversal(root):
    ret=[]
    stack=[(root,False)]
    
    while stack:
        cur_node,visited=stack.pop()
        if cur_node:
            if not visited:
                stack.append((cur_node.right,False))
                stack.append((cur_node,True))
                stack.append((cur_node.left,False))
            else:
                ret.append(cur_node.val)
            
    return ret
