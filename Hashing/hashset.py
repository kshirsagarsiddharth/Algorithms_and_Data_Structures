class MyHashSet:
    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]
    
    def add(self,key):
        bucket,idx = self._index(key)
        if idx >= 0:
            return 
        bucket.append(key)
    
    def remove(self,key):
        bucket,idx = self._index(key)
        if idx < 0:
            return
        bucket.remove(key)
    
    def contains(self,key):
        _,idx = self._index(key)
        return idx >= 0
    
    def _hash(self,key):
        return key % self.size
    
    def _index(self,key):
        hash_value = self._hash(key)
        bucket = self.buckets[hash_value]
        for i,k in enumerate(bucket):
            if k == key:
                return bucket,i
        return bucket,-1
a = set()
a.

