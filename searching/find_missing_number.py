# %%

array = [1,2,3,4,6,7,8,9]
for i in range(len(array) - 1):
    if array[i] != array[i + 1] - 1:
         print(array[i] + 1)
         break
# the complexicity for this is O(nlog(n)

# %%
# Method 2
def sum_using_natural_numbers(array,n):
    sum_formula = ((n + 2) * (n + 1)) // 2
    array_sum = sum(array)
    ans = sum_formula - array_sum
    return ans

sum_using_natural_numbers(array,len(array))


# %%
def  sum_using_natural_numbers_without_overflow(array,n):
    total = 1
    for i in range(2,n + 2):
        total += i
        total -= array[i - 2]
    return total

array = [1,2,3,4,6,7,8,9]
n = len(array)
print(sum_using_natural_numbers_without_overflow(array,n))

# %%
def find_missing_no_using_xor(array,n):
    x1 = 1
    y1 = array[0]
    for i in range(1,n):
        y1 = y1 ^ array[i]
    
    for i in range(2,n + 2):
        x1 = x1 ^ i
    
    return x1 ^ y1
array = [1,2,3,4,6,7,8,9]
n = len(array)
print(find_missing_no_using_xor(array,n))
