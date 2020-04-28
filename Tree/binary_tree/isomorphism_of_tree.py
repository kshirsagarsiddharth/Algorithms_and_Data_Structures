class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
def isomorphic(root1,root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False
    if root1.data != root2.data:
        return False
    return (isomorphic(root1.left,root2.left) and isomorphic(root1.right,root2.right)) or (isomorphic(root1.left,root1.right) and isomorphic(root1.right,root2.left))