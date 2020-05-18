def dutch_national_flag_problem(array,n):
    left = 0
    right = n - 1
    mid = 0

    while mid < right:
        if array[mid] == 0:
            array[left],array[mid] = array[mid],array[left]
            mid += 1
            left += 1
        
        elif array[mid] == 1:
            mid += 1
        
        else: # array[mid] == 2:
            array[right],array[mid] = array[mid],array[right]
            right -= 1

