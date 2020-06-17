"""
Method one using recursion
"""

def validate(root,lower = float("-inf"),higher = float("inf")):
    if not root:
        return True
    
    val = root.val

    if val <= lower or val >= higher:
        return False
    
    if not validate(root.left,lower,val):
        return False
    
    if not validate(root.right,val,higher):
        return False
    
    return True

"""
Validate binary search tree using iteration
"""

def validate(root):
    if not root:
        return True
    
    stack = [(root,float("-inf"),float("inf"))]
    while stack:
        root,lower,upper = stack.pop()
        if not root:
            continue
        val = root.val

        if val <= lower or val >= upper:
            return False
        
        stack.append((root.left,lower,val))
        stack.append((root.right,val,upper))
    
    return True

        
