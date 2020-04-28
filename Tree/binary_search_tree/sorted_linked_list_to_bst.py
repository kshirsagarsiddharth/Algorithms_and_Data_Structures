class DNode:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

def doubally_linked_list_to_BST(head):
    if head is None or head.next is None:
        return head
    temp = middle_node(head)
    P = head
    while P.next != temp:
        P = P.next
    P.next = None
    Q = temp.next
    temp.next = None
    temp.prev = doubally_linked_list_to_BST(head)
    temp.next = doubally_linked_list_to_BST(Q)
    return temp

def middle_node(head):
    slow_ptr = head
    fast_ptr = head
    while fast_ptr and fast_ptr.next:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next
    return slow_ptr

"""
def middle_node(head):
	if head is None:
		return None
	slow_ptr = head
	fast_ptr = head
	while fast_ptr and fast_ptr.next:
		slow_ptr = slow_ptr.next
		fast_ptr = fast_ptr.next.next 
	return slow_ptr

def ll_to_bbst(head):
	if head is None or head.next is None:
		return head
	temp = middle_node(head)
	P = head
	while(P.next is not temp):
		P = P.next
	P.next = None
	Q = temp.next 
	temp.next = None
	temp.prev = ll_to_bbst(head)
	temp.next = ll_to_bbst(Q)

	return temp
"""

