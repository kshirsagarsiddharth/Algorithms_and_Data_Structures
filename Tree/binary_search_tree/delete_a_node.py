class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def delete_node(root,data):
    # if the root dosenot exist just return the root
    if root is None:
        return root
    # find the node in the left subtree if the root value is greater than
    # the node to be deleted  value
    if root.data > data:
        root.left = delete_node(root.left,data)
    # find the node in the right tree is the root value is less than the node to be deleted
    elif root.data < data:
        root.right = delete_node(root.right,data)
    
    else:
        #if there is no right children delete the node and the new root would be root.left
        if root.right is None:
            return root.left
        # if there is no left children delete the node and the new root 
        #would be root.right
        if root.left is None:
            return root.right

        # if both left and right childrens of the node exists replace its value with the minimum value in the right subtree. and after replacing delete that minimum node in the right subtree

        temp_val = root.right
        while temp_val.left:
            temp_val = temp_val.left

        # replace the value
        root.data = temp_val.data   

        root.right = delete_node(root.right,root.data)

    return root


    