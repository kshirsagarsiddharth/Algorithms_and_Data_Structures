class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def delete_whole_tree_recursively(root):
    if root  == None:
        return
    delete_whole_tree_recursively(root.left)
    delete_whole_tree_recursively(root.right)
    print(root.data)
    del root

root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
delete_whole_tree_recursively(root)