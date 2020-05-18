import sys
def min_abs_sum_brute_force(array,n):
    """
    python program to find the minimum absolute
    sum or elements whose sum is close to zero
    """
    min_one = 0
    min_two = 0
    min_sum = array[0] + array[1]

    for i in range(0,n - 1):
        for j in range(i + 1,n):
            if abs(array[i] + array[j]) < abs(min_sum):
                min_sum = abs(array[i] + array[j])
                min_one = i
                min_two = j
    return array[min_one],array[min_two]

arr = [1, 60, -10, 70, -80, 85] 

def min_abs_sum_optimal(array,n):
    array.sort()
    left = 0
    right = n - 1
    min_l = 0
    min_r = 0
    Sum = 0
    min_sum = sys.maxsize

    while left < right:
        Sum = array[left] + array[right]

        if abs(Sum) < min_sum:
            min_sum = Sum
            min_l = left
            min_r = right
        
        if Sum > 0:
            right -= 1
        else:
            left += 1
    
    return array[min_l],array[min_r]


        