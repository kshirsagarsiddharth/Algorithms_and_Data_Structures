# python class that represents a individual node in a binary tree
class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

root = Node(1)
print(root)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root