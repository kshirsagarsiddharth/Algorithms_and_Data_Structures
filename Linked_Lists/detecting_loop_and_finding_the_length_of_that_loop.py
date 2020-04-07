# -*- coding: utf-8 -*-

# program to find the length of loop in a linked list
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert_node(self,new_data):
        if self.head == None:
            self.head = Node(new_data)
        else:
            current = self.head
            while(current.next):
                current = current.next
            current.next = Node(new_data)
            
    #Coding a function which creates a loop in the linked list
    # this function creates loop by connecting last node to nth node of the linked list
    # counting first node as 1
    
    def create_loop(self,n):
        loop_node = self.head
        # in this case we are traversing until range n
        for i in range(0,n):
            loop_node = loop_node.next
            
        tail_node = self.head
        while(tail_node.next):
            tail_node = tail_node.next
            
        tail_node.next = loop_node
        
    # this function detects loop and returns the length of the loop
    # if the returned length has vaklue zero, than the linked list is empty
    # or there is no existance of a loop.
    
    def detect_loop(self):
        # if the linked list is empty then there is no loop
        # so we return zero
        if self.head is None:
            return 0
        
        # using floyds algorithm for loop detection and finding length
        slow = self.head
        fast = self.head
        flag =0 # to show both fast and slow are at the same position
        
        while (slow and slow.next and fast and 
               fast.next and fast.next.next):
            if slow == fast and flag != 0:
                # if this condition is satiisfied the loop in conformed
                # and this means that fast and slow are at same position
                count = 1
                slow = slow.next
                while(slow != fast):
                    slow = slow.next
                    count += 1
                return count
            
            slow = slow.next
            fast = fast.next.next
            flag = 1
        return 0 # there is no loop
    
    def find_first_element(self):
        # if the linked list is empty then there is no loop
        # so we return zero
        if self.head is None:
            return 0
        
        # using floyds algorithm for loop detection and finding length
        slow = self.head
        fast = self.head
        flag =0 # to show both fast and slow are at the same position
        
        while (slow and slow.next and fast and 
               fast.next and fast.next.next):
            if slow == fast and flag != 0:
                # if this condition is satiisfied the loop in conformed
                # and flag means that fast and slow are not at same position
                
                
                # if loop is found initialize slow pointer to head
                # move both slow and fast pointer one at a time
                # the point at which they meet is the starting positiion
                slow = slow.head
                while(slow!= fast):
                    slow = slow.next
                    fast = fast.next
                return slow
                
            
            slow = slow.next
            fast = fast.next.next
            flag = 1
        return 0 # there is no loop

# Setting up the code 
# Making a Linked List and adding the nodes 
ll = LinkedList() 
ll.insert_node(1)
ll.insert_node(1)
ll.insert_node(1)
ll.insert_node(1)
ll.insert_node(1)
ll.insert_node(1)

# Creating a loop in the linked List 
# Loop is created by connecting the 
# last node of linked list to n^th node 
# 1<= n <= len(LinkedList) 
ll.create_loop(2) 

# Checking for Loop in the Linked List 
# and printing the length of the loop 
loop_length = ll.detect_loop()
print(loop_length)

# This code is contributed by _Ashutosh 
                
    
        
                            
            
            
