class Deque:
    def __init__(self):
        self.de_que = []

    def enque_front(self,data):
        self.de_que.append(data)
    
    def enque_rear(self,data):
        self.de_que.insert(0,data)
    
    def deque_front(self):
        self.de_que.pop()

    def deque_rear(self):
        self.de_que == []
    
    def size(self):
        return len(self.de_que)
    
    def is_empty(self):
        return self.de_que == []
    
def palindrom_checker(characters):
    de = Deque()
    for val in characters:
        de.enque_rear(val)
    
    while not de.is_empty():
        first = de.deque_front()
        last = de.deque_rear()
        if first != last:
            return False
        
    return True

print(palindrom_checker('radar'))



