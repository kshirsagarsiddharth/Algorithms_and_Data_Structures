class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # add new value to the linked using lpush

    def lpush(self,new_value):
        new_node = Node(new_value)

        if self.head is None:
            self.head = new_node
            return
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next 

        curr_node.next = new_node

    def merge_linked_lists(self,list1,list2):
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        if list1.data < list2.data:
            result = list1
            result.next = self.merge_linked_lists(list1.next,list2)
        else:
            result = list2
            result.next = self.merge_linked_lists(list1,list2.next)
        
        return result

    
    def get_middle(self,head):
        if head is None:
            return head
        slow = head
        fast = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next 
        return slow
    
    def merge_sort(self,List):
        if List is None and List.next is None:
            return List
        middle = self.get_middle(List)
        next_to_middle = middle.next 
        middle.next  = None
        left = self.merge_sort(List)
        right = self.merge_sort(next_to_middle)

        sorted_list = self.merge_linked_lists(left,right)
        return sorted_list    
def print_list(head):
    if head is None:
        print(' ')
        return
    curr_node = head
    while curr_node:
        print(curr_node.data)
        curr_node = curr_node.next
    print(' ')

