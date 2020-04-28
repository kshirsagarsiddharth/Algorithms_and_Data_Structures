class Node:
    def __init__(self,data = None):
        self.data = data
        self.left = None
        self.right = None
def build_balenced_tree(l,r):
    mid = l + (r - l) // 2
    node = Node()
    if l > r:
        return None
    node.left = build_balenced_tree(l,mid - l)
    node.right = build_balenced_tree(mid + l,r)
    node.data = mid
    return node

build_balenced_tree(1,7)
