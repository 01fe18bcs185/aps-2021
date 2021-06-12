# Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

def buildTree(inorder, postorder):
    if not inorder or not postorder:
        return None
    root = TreeNode(postorder.pop())
    inorder_idx = inorder.index(root.val)
    
    root.right = buildTree(inorder[inorder_idx+1:], postorder) 
    root.left = buildTree(inorder[:inorder_idx], postorder)
    
    return root

