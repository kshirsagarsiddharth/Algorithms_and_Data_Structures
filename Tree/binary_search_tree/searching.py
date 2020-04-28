class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

def search_recursive(root,data):
    if root is None:
        return None
    if root.data == data:
        return root
    elif root.data > data:
        return search_recursive(root.left,data)
    else:
        return search_recursive(root.right,data)
 
def search_iteratively(root,data):
    if root is None:
        return None
    while root is not None:
        if root.data == data:
            return root
        elif root.data > data:
            root = root.left
        elif root.data < data:
            root = root.right
        else:
            return False

def insert_recursively(root,data):
    if root is None:
        return Node(data)
    else:
        if data < root.data:
            if root.left is None:
                root.left = Node(data)
            else:
                insert_recursively(root.left,data)
        else:
            if root.right is None:
                root.right = Node(data)
            else:
                insert_recursively(root.right,data)
    
root = None
root = insert_recursively(root, 50)  
insert_recursively(root, 30)  
insert_recursively(root, 20)  
insert_recursively(root, 40)  
insert_recursively(root, 70)  
insert_recursively(root, 60)  
insert_recursively(root, 80) 
print(search_iteratively(root,60).data)