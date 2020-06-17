def permute(nums):
    res = []
    def helper(nums,path,res):
        if not nums:
            res.append(path)
        for i in range(len(nums)):
            helper(nums[:i] + nums[i + 1:],path + [nums[i]],res)
    helper(nums,[],res)
    return res