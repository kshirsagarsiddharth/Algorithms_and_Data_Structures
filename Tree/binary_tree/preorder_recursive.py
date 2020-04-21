
'''Pre-Order Tree Traversal

In this traversal method, the root node is visited first, then the left sub tree
Then the right sub tree

In the following program we use the Node class to create place holders for the
root node as well as left and right nodes.

Then we create a insert function to add data to the tree.
Finally the preorder traversal logic is implemented by creating an empty
list and adding the root nodes first followed by the left node.
At last the right node is added to compleat the preordder traversal.
This process is repeated fro each subtree until all the nodes are traversed.
'''

class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
    # inserting the node in a tree
    def insert(self,data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = Node(data)

    def pre_order_traversal(self,root):
        result = []
        if root:
            result.append(root.data)
            result = result + self.pre_order_traversal(root.left)
            result = result + self.pre_order_traversal(root.right)
        return result

root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
print(root.pre_order_traversal(root))
    
