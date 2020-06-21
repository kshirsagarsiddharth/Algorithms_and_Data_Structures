"""
nearby duplicates using sliding window
"""

def contains_nearby(nums: List[int],k: int) -> bool:
    window = set()
    for i,val in enumerate(nums):
        if len(window) >= k + 1:
            window.remove(nums[i - k - 1])
        if val in window:
            return True
        window.add(val)
    return False

def containsNearbyduplicates(nums: List[int],k: int) -> bool:
    dic = dict()
    for i,val in enumerate(nums):
        if val in dic and i - dic[val] <= k:
            return True
        dic[val] = i
    return False