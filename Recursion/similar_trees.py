def isSameTree(p,q):
    if not p and not q:
        return True
    
    if not p or not q:
        return False
    
    if p.val != q.val:
        return False
    
    return isSameTree(p.left,q.left) and isSameTree(p.right,q.right)

"""
Iterative Version
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def check(p,q):
            if not p and not q:
                return True

            if not p or not q:
                return False

            if p.val != q.val:
                return False
            return True
        dq = []
        dq.append((p,q))
        while dq:
            p,q = dq.pop(0)
            if not check(p,q):
                return False
            if p and q:
                dq.append((p.left,q.left))
                dq.append((p.right,q.right))
        return True
        
        #return True

        

        
    