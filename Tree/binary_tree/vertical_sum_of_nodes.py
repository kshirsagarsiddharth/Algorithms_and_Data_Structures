class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
hash_table = {}
def vertical_sum_in_binary_tree(root,column):
    if root is None:
        return
    if column not in hash_table:
        hash_table[column] = 0
    hash_table[column] += root.data
    vertical_sum_in_binary_tree(root.left,column - 1)
    vertical_sum_in_binary_tree(root.right,column + 1)
    