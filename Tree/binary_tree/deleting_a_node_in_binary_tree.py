class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data)
    inorder(root.right)

# function to delete the given deepest node in a binary tree
def deleting_the_given_node(root,d_node):
    queue = []
    queue.append(root)
    while len(queue) > 0:
        temp = queue.pop(0)
        if temp is d_node:
            temp = None
            return
        if temp.right is not None:
            if temp.right is d_node:
                temp.right = None
                return
            else:
                queue.append(temp.right)
        if temp.left is not None:
            if temp.left is d_node:
                temp.left  = None
                return
            else:
                queue.append(temp.left)

def delete_a_particular_node(root,data):
    if root is None:
        return None
    if root.left is None and root.right is None:
        if root.data == data:
            return None
        else:
            return root

    key_node = None
    queue = []
    queue.append(root)
    while len(queue) > 0:
        temp = queue.pop(0)
        if temp.data == data:
            key_node = temp
        if temp.left is not None:
            queue.append(temp.left)
        if temp.right is not None:
            queue.append(temp.right)
        
    if key_node is not None:
        x = temp.data
        deleting_the_given_node(root,temp)
        key_node.data = x
    return root



root = Node(10) 
root.left = Node(11) 
root.left.left = Node(7) 
root.left.right = Node(12) 
root.right = Node(9) 
root.right.left = Node(15) 
root.right.right = Node(8) 
delete_a_particular_node(root,11)
        
        