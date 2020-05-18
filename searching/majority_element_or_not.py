import sys
def find_majority_bruteforce(array):
    index = -1
    max_count = -(sys.maxsize)
    for i in range(0,len(array) - 1):
        count = 0
        for j in range(0,len(array)):
            if array[i] == array[j]:
                count += 1
        
        if count > max_count:
            max_count = count
            max_ind = i
        
    
    if max_count > len(array) / 2:
        print(array[index],max_count)
        return True
    return False

"""
The above approach has complexicity of O(n * n)
"""
# APPROACH 2
"""
if a given element is a majority element than  than that element will lie at the middle of the array if the array is sorted
this approach takes O(n * logn)
"""


def majority_elem_approach_two(array,n):
    array.sort()
    mid = n // 2
    count = 0
    elem = array[mid]
    for i in range(0,n):
        if array[i] == elem:
            count += 1
    
    if count > n / 2:
        return True
    
    return False
arr = [2, 2, 2, 2, 5, 5, 2, 3, 3]  
n = len(arr) 
print(majority_elem_approach_two(arr,n))


"""
This approach uses hash maps with time O(n) and space O(n)
"""
def majotity_elem_approach_three(array,n):
    dic = dict()
    for i in range(0,n):
        if array[i] in dic:
            dic[arr[i]] += 1
        else:
            dic[arr[i]] = 1

    for key,val in dic.items():
        if val > n / 2:
            return key,val

"""
This approach uses moors therom with complexicity O(n)
"""
def majority_elem_approach_four(array,n):
    maj_index = 0
    count = 1
    for i in range(len(array)):
        if array[maj_index] == array[i]:
            count += 1
        else:
            count -= 1
        
        if count == 0:
            maj_index = i
            count = 1
    return array[maj_index]

