def segregate_even_and_odd(array,n):
    left = 0
    right = n - 1

    while left < right:
        while array[left] % 2 == 0 and left < right:
            left += 1
        
        while array[right] % 2 == 1 and left < right:
            right -= 1

        if left < right:
            (array[left],array[right]) = (array[right],array[left])

            left += 1
            right -= 1

def segregate_ones_and_zeros(array,n):
    
    left = 0
    right = n - 1

    while left < right:
        
        while array[left] == 0 and left < right:
            left += 1
        
        while array[right] == 1 and left < right:
            right -= 1
        
        if left < right:
            (array[left],array[right]) = (array[right],array[left])

            left += 1
            right -= 1

arr = [ 0, 1, 0, 1, 1, 1 ] 
n = len(arr)

segregate_ones_and_zeros(arr,n)
print(arr)


        