# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

def buildTree(preorder, inorder):
    
    def dfs(preorder, inorder):
        if preorder and inorder:
            root = TreeNode(preorder[0])
            idx = inorder.index(root.val)

            root.left = dfs(preorder[1:idx+1], inorder[:idx])
            root.right = dfs(preorder[idx+1:], inorder[idx+1:])

            return root
    
    return dfs(preorder, inorder)
