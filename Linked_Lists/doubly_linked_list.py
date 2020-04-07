class Node:
    # Initializing python constructor which has parameters as data of a node and two pointers next and previous
    def __init__(self,data = None,next = None,prev = None):
        self.data = data  # data initialized to data (data of node of the list)
        self.next = next  # next pointer of the list
        self.prev = prev  # previous pointer of the list
        self.head = None  # first node or head node of the linked list initialized to zero
        self.tail = None  # last node of the linkedlist initialized to none
        self.length = 0   # length of the linked list
    
    def set_data(self,data = None): # in this case we enter data in set_data function and data in given object will get initialized
        self.data = data
        
    def get_data(self):
        return self.data
    
    def set_next(self,next = None):
        self.next = next
    
    def get_next(self):
        return self.next
    # we use this function to find wether the list has next node by observing the logic of the function we understand that
    # this function returns a boolean value i.e it returns true if next element in the list dosen't have none else 
    # else it returns false
    def has_next(self):   
        return self.next is not None
    
    def set_prev(self,prev = None):
        self.prev = prev
        
    def get_prev(self):
        return self.prev
    
    def has_prev(self):
        return self.prev is not None
    
    def list_length(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()
        return count
    
    def print_linked_list(self):
        if self.head is None:
            print('The linked list dose not exist')
        else:
            current = self.head
            while current is not None:
                print(current.get_data())
                current = current.get_next()
                
    def insert_at_beginning(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node # in this case we are defining two nodes one is 
            # head node and the other one is tail. When we check and find thet there is no list present
            # we make the new node as head and tail of our linked list.
        else:
            new_node.set_next(self.head)
            new_node.set_prev(None)
            self.head.set_prev(new_node)
            self.head = new_node
        self.length += 1
    
    def insert_at_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node # making new node as head as well as tail in our double ll
        else:
            current = self.head
            while current.get_next() is not None:
                current = current.get_next() # after the loop is executed last node is stored in current variable
            current.set_next(new_node)
            new_node.set_prev(current)
            new_node.set_next(None)
            self.tail = new_node
        self.length += 1
        
        # here we have + 1 because we are inserting in the end and in a linked list when we insert at the 
        # end position we get a extra index number hence we have +1 for length
        
    def insert_at_position(self,data,position):
        if position < 0 or position > self.length + 1:
            raise ValueError('Invalid Position')
        elif position == 0:
            self.insert_at_beginning(data)
        elif position == self.length + 1:
            self.insert_at_end(data)
        else:
            new_node = Node(data)
            count = 1
            current= self.head
            while count != position:
                current = current.get_next()
                count += 1
            new_node.set_next(current)
            new_node.set_prev(current.get_prev())
            current.get_prev().set_next(new_node)
            current.set_prev(new_node)
            self.length += 1
            
    def delete_from_beginning(self):
        if self.head is None:
            raise ValueError('The Linked List is Not Defined')
        else:
            current = self.head
            self.head = current.get_next()
            current.set_next(None)
            self.head.set_prev(None)
            self.length -= 1
    
    def delete_from_end(self):
        if self.head is None:
            raise ValueError('Linked list is not defined')
        else:
            current = self.tail
            self.tail = current.get_prev()
            current.set_prev(None)
            self.length -= 1
    
    def delete_at_position(self,position):
        if self.head is None:
            raise ValueError('Linked List is Empty')
        elif position < 1 or position > self.length:
            raise ValueError('You have entered a invalid position')
        elif position == 1:
            self.delete_from_beginning()
        elif position == self.length:
            self.delete_from_end()
        else:
            count = 1
            current = self.head
            previous = None
            while count != position:
                previous = current
                current = current.get_next()
                count += 1
            previous.set_next(current.get_next())
            current.get_next().set_prev(previous)
            current.set_prev(None)
            current.set_next(None)
            self.length -= 1



        
        




































            
            
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
            
            
    
   
   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
            
                
            
        
                
                
     



































           
            