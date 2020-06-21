class HashTable:
    def __init__(self):
        self.max_length = 8
        self.table = [None] * self.max_length
    
    
    def set_item(self,key,value):
        hashed_key = self.hash(key)
        while self.table[hashed_key] is not None:
            if self.table[hashed_key][0] == key:
                break
            hashed_key = self.increment_key(hashed_key)
        temp = (key,value)
        self.table[hashed_key] = temp

    def find_item(self,key):
        hashed_key = self.hash(key)
        if self.table[hashed_key] is None:
            raise KeyError
        if self.table[hashed_key][0] != key:
            original_key = hashed_key
            while self.table[hashed_key][0] != key:
                hashed_key = self.increment(hashed_key)
                if self.table[hashed_key] is None:
                    raise KeyError
                if hashed_key == original_key:
                    raise KeyError
        return hashed_key        
    
    def hash(self,key):
        return key % self.max_length
    
    def increment(self,key):
        return (key + 1) % self.max_length
    
    

     






t = {}
t['asdf'] = 'alpha'
t['08gh'] = 'bravo'
t['hysortj'] = 'charlie'
t['1234asdhfl'] = 'dog'
t['asdflkjh'] = 'else'
t['5ohslafj'] = 'find'