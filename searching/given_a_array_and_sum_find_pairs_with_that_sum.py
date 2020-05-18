def check_for_pair_method_one(array,k):
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        if array[left] + array[right] == k:
            return 1
        elif array[left] + array[right] > k:
            right -= 1
        else:
            left += 1
    return 0

def check_for_pairs_method_two(array,k):
    s = set()
    for i in range(len(array)):
        temp = k - array[i]
        if temp in s:
            print(array[i],temp)
        s.add(array[i])

array = [1, 4, 45, 6, 10, -8] 
n = 16

check_for_pairs_method_two(array,n)
