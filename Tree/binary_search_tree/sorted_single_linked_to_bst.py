class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None
class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None


def convert_ll_to_array(head):
    values = []
    while head is not None:
        values.append(head.val)
        head = head.next 
    return values

def sorted_linked_list_to_BST(head):
    values = convert_ll_to_array(head)

    def sorted_linked_list_to_BST_util(left,right):
        if left > right :
            return None
        middle = (left + right) // 2
        node = TreeNode(values[middle])

        # only one element is left in the array
        if left == right:
            return node
        
        node.left = sorted_linked_list_to_BST_util(left,middle - 1)
        node.right = sorted_linked_list_to_BST_util(middle + 1,right)

        return node
    return sorted_linked_list_to_BST_util(0,len(values) - 1)


    