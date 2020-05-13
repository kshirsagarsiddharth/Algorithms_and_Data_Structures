"""
Method 1 brute force
"""
class BruteForce:
    def __init__(self,array):
        self.array = array
        self.size = len(array)
    def repeated_elements(self):
        for i in range(self.size):
            for j in range(i + 1,self.size):
                if self.array[i] == self.array[j]:
                    return True
        
        return False

class Optimized:
    def __init__(self,array):
        self.array = array
        self.size = len(array)
    def repeated_elements(self):
        self.array.sort()
        for i in range(self.size):
                if self.array[i] == self.array[i + 1]:
                    return True
        
        return False
array = [1,5,6,8,45,7,0,9,7,9]

bf = Optimized(array)
print(bf.repeated_elements())
