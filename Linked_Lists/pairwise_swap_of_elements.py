# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 01:14:50 2020

@author: siddharth
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_from_beginning(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node


    def print_linked_list(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next
    
    def pairwise_swap_of_elements(self):
        current = self.head
        while(current is not None and current.next is not None):
            current.data,current.next.data = current.next.data,current.data
            current = current.next.next
    
ll = LinkedList()
for i in range(0,110000):
    ll.insert_from_beginning(i)

ll.pairwise_swap_of_elements()
ll.print_linked_list()
    