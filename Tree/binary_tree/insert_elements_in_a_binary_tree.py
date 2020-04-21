class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
def inorder(root):
    if root is None:
        return 
    inorder(root.left)
    print(root.data,end = " ")
    inorder(root.right)

def insert_level_order(root,data):
    queue = []
    queue.append(root)
    # lets do level order traversal until we find the 
    # first empty node
    while len(queue) != 0:
        temp = queue.pop(0)
        if temp.left is None:
            temp.left = Node(data)
            break
        else:
            queue.append(temp.left)
        if temp.right is None:
            temp.right = Node(data)
            break
        else:
            queue.append(temp.right)

root = Node(2) 
root.left = Node(7) 
root.right = Node(5) 
root.left.left = Node(8)
root.left.right = Node(9)
root.right.left = Node(10)
root.right.right = Node(11)

insert_level_order(root,56)

inorder(root)