def reverse_string(s):
    def helper(left,right):
        if left > right:
            return s
        return helper(left + 1,right - 1)
    
    return helper(0,len(s) - 1)