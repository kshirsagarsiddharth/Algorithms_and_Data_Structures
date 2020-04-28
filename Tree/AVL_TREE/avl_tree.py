import sys

class AVLNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

class AVL_tree:


    def get_height(self,root):
        if root is None:
            return 0 
        return root.height
    
    def get_balence(self,root):
        if root is None:
            return 0
        
        return self.get_height(root.left) - self.get_height(root.right)
    
    def pre_order(self,root):
        if root is None:
            return
        print("{}".format(root.data),end = " ")
        self.pre_order(root.left)
        self.pre_order(root.right)
    
    def left_rotate(self,z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.get_height(z.left),self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left),self.get_height(y.right))

        return y

    def right_rotate(self,z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3 


        z.height = 1 + max(self.get_height(z.left),self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left),self.get_height(y.right))

    
    def insert_node(self,root,data):
        if root is None:
            return AVLNode(data)
        
        elif data < root.data:
            root.left = self.insert_node(root.left,data)
        
        else: # data > root.data
            root.right = self.insert_node(root.right,data)

        root.height = 1 + max(self.get_height(root.left),self.get_height(root.right))
        balence_factor = self.get_balence(root)

        if balence_factor > 1:
            if data < root.left.key:
                return self.right_rotate(root)
            else:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)
        
        if balence_factor < -1:
            if data > root.right.data:
                return self.left_rotate(root)
            else:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)
        return root
    
    def delete_node(self,root,data):
    # if the root dosenot exist just return the root
        if root is None:
            return root
        # find the node in the left subtree if the root value is greater than
        # the node to be deleted  value
        if root.data > data:
            root.left = self.delete_node(root.left,data)
        # find the node in the right tree is the root value is less than the node to be deleted
        elif root.data < data:
            root.right = self.delete_node(root.right,data)
        
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

            root.right = self.delete_node(root.right,root.data)

            if root is None:
                return root
            
            root.height = 1 + max(self.get_height(root.left),self.get_height(root.right))
            balence_factor = self.get_balence(root)
            if balence_factor > 1:
                if self.get_balence(root.left) >= 0:
                    return self.right_rotate(root)
                else:
                    root.left = self.left_rotate(root.left)
                    return self.right_rotate(root)
                
            if balence_factor < -1:
                if self.get_balence(root.right) <= 0:
                    return self.left_rotate(root)
                else:
                    root.right = self.right_rotate(root.right)
                    return self.left_rotate(root)

        return root

    