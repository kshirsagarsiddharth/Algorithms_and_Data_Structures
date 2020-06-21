"""
solution one
"""

def find_restraunts(list1,list2):
    List1 = {u:i for i,u in enumerate(list1)}
    best,ans = float("inf"),[]

    for j,v in enumerate(list2):
        i = List1.get(v,float("inf"))
        if i + j < best:
            best = i + j
            ans = [v]
        elif i + j == best:
            ans.append(v)
    return ans

"""
solution two

"""

def findRestraunts(list1,list2):
    rest2_to_index = {rest2 : index2 for index2,rest2 in enumerate(list2)}
    common_intrests = {}

    for index1,rest1 in enumerate(list1):
        if rest1 in rest2_to_index:
            common_intrest[rest1] = rest2_to_index[rest1] + index1
    
    least_index = min(common_intrests.values())
    result = [rest for rest in common_intrests if common_intrests[rest] == least_index]
    return result