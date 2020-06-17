def swap_pairs(head):
    if head and head.next:
        temp = head.next 
        head.next = swap_pairs(temp.next)
        temp.next = head
        return temp
    return head

class ListNode:
    pass
def swap_pairs_iterative(self,head):
    if not head or not head.next:
        return head
    dummy = ListNode(0)
    dummy.next = head
    curr = dummy
    while curr.next and curr.next.next:
        first = curr.next
        second = curr.next.next 
        curr.next = second
        first.next = second.next 
        second.next = first 
        curr = curr.next.next 
    return dummy.next 