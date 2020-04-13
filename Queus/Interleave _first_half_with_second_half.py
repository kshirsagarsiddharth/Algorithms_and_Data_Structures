class Que:
    def __init__(self,capacity):
        self.front = self.size = 0
        self.rear = capacity - 1
        self.queue = [None] * capacity
        self.capacity = capacity
        
    # the queue is full when the size becomes equall to capacity
    def is_full(self):
        return  self.size == self.capacity
    
    # the  queue is empty when the size is equal to zero
    
    def is_empty(self):
        return self.size == 0
    
    # function to add an item to the queue
    # this changes the size and the rear of the queue
    def en_que(self,data):
        if self.is_full():
            print('the queue is full')
            return
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = data
        self.size += 1
        print('The item enqueued to the queue is {}'.format(data))
        
    # function to remove the item from the queue
    def de_que(self):
        if self.is_empty():
            print('The queue is empty')
            return
        else:
            print('the item dequed is {}'.format(self.queue[self.front]))
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.capacity
            self.size = self.size - 1
        
        return temp
    
    def que_front(self):
        if self.is_empty():
            print('the queue is empty')
            return
        else:
            print('the front item is {}'.format(self.queue[self.front + 1]))
    
    def que_rear(self):
        if self.is_empty():
            print('the queue is empty')
            return
        else:
            print('the rear of the queue is {}'.format(self.queue[self.rear]))
def interleaving_qs(queus):
    # check wether the elements of the queue are even
    if queus.size % 2 != 0:
        print('need even fumbers to proceed')
        return
    # initializing the empty stack
    aux = []
    half_size = queus.size // 2
    # deque the first half and push it onto the stack
    for i in range(int(half_size)):
        aux.append(queus.de_que())
    
    # pop fom the stack and enque it back on the queue
    while(len(aux) != 0):
        queus.en_que(aux[-1])
        aux.pop()
    
    aux.append(queus.de_que())
    queus.en_que(aux[-1])
    aux.pop()

    for i in range(int(half_size)):
        aux.append(queus.de_que())
    
    while(len(aux) != 0):
        queus.en_que(aux[-1])
        aux.pop()

    return queus.que_front(),queus.que_rear()

q = Que(10)
q.en_que(1)
q.en_que(2)
q.en_que(3)
q.en_que(4)

interleaving_qs(q)
















