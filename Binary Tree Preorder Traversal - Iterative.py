 def preorderTraversalroot):
    ret=[]
    stack=[root]
    
    while stack:
        cur_node=stack.pop()
        if cur_node:
            ret.append(cur_node.val)
            stack.append(cur_node.right)
            stack.append(cur_node.left)
    return ret
