def maxDepth(root):
    stack,max_depth = [(root,1)],0
    while stack:
        node,level = stack.pop()
        if node:
            max_depth = max(max_depth,level)
            stack.append((node.left,level + 1))
            stack.append((node.right,level + 1))
    
    return max_depth