def combinations(n,k):
    result = []
    combination_helper(range(n + 1),k,0,[],result)
    return result

def combination_helper(nums,k,index,path,result):
    if k == 0:
        result.append(path)
        return
    
    for i in range(index,len(nums)):
        combination_helper(nums,k - 1,i + 1,path + [nums[i]],result)