 def postorderTraversal(root):
    ret=[]
    stack=[(root,False)]
    
    while stack:
        node,visited=stack.pop()
        if node:
            if not visited:
                stack.append((node,True))
                stack.append((node.right,False))
                stack.append((node.left,False))
                
            else:
                ret.append(node.val)
    return ret
