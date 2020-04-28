class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def inorder_sucessor(root,node):
    # case 1 if the node has right sub tree than find the 
    # least value node from that right subtree
    if node is None:
        return
    if node.right is not None:
        temp = node.right
        while(temp.left is not None):
            temp = temp.left
        return temp.data
    # if the node dosenot have a right subtree search the node from root the node from
    # where we take the last left is the answer 
    else:
        S = root
        while S.data is not node.data:
            if node.data < S.data:
                store = S
                S = S.left
            else:
                S = S.right
        return store
    
        """
        S = root
        while S.data is not node.data:
            if S.data > node.data:
                result = S
                S = S.left
            else:
                S = S.right
        """
def inorder_predecessor(root,node):
    # if the node has left sub tree
    # than jump to that left subtree and go to the rightmost node 
    if node.left is not None:
        temp = node.left
        while temp.right is not None:
            temp = temp.right
        return temp
    # if the node dosenot have left subtree, search that node from the root,
    #  and node from where we take the last right is the answer.
    else:
        S = root
        while node.data != root.data:
            if node.data < root.data:
                S = S.left
            else:
                store = S
                S = S.right
        return store
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
    

  
# Creating the tree given in the above diagram 
def insert( node, data): 
  
    # 1) If tree is empty then return a new singly node 
    if node is None: 
        return Node(data) 
    else: 
         
        # 2) Otherwise, recur down the tree 
        if data <= node.data: 
            temp = insert(node.left, data) 
            node.left = temp  
            temp.parent = node 
        else: 
            temp = insert(node.right, data) 
            node.right = temp  
            temp.parent = node 
          
        # return  the unchanged node pointer 
        return node 
  
  
# Driver progam to test above function 
  
root  = None
  
# Creating the tree given in the above diagram  
root = insert(root, 20) 
root = insert(root, 8); 
root = insert(root, 22); 
root = insert(root, 4); 
root = insert(root, 12); 
root = insert(root, 10);   
root = insert(root, 14);     
temp = root.left.right.right  
inorder_sucessor(root,temp).data