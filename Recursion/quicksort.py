def quick_sort(nums,low,high):
    if not nums:
        return nums
    
    while low < high:
        p = partition(nums,low,high)
        quick_sort(nums,low,p - 1)
        quick_sort(nums,p + 1,high)


def partition(nums,low,high):
    pivot = nums[high]
    i = low
    for j in range(low,high):
        if nums[j] < pivot:
            nums[i],nums[j] = nums[j],nums[i]
    
    nums[high],nums[i] = nums[i],nums[high]

    return i