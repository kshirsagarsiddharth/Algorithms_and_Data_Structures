"""
Given the values as input add the values in the datastructure this is function one next is 
given the vasues find wether the given values in the dictonary add up to given input keep in mind that if the
given value is repeated only once it can be used only once in the sum
"""
class ImplementTwosum:
    def __init__(self):
        self.dic = dict()
    
    def add(self,val: int) -> None:
        self.dic[val] = self.dic.get(val,0) + 1
    
    def find(self,target: int) -> bool:
        for val in self.dic:
            comp_val = target - val
            if comp_val == val and self.dic[comp_val] > 1:
                return True
            elif comp_val in self.dic:
                return True
    
        return False