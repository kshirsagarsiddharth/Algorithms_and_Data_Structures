def count_sort_method_one(array):
    k = max(array)
    n = len(array)
    count = [0] * (20)
    output = [None] * n
   
    for i in range(0,n):
        count[array[i]] += 1
    for i in range(1,k + 1):
        count[i] = count[i] + count[i - 1]
    
    for i in range(n - 1,-1,-1):
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
    for i in range(0,n):
        array[i] = output[i]
    
data = [4, 2, 2, 8, 3, 3, 1]

count_sort_method_one(data)
print(data)

"""
def counting_sort(array):
    n = len(array)
    k = max(array)
    count = [0] * (k + 7)
    output = [None] * (n)
    for i in range(0,n):
        count[array[i]] += 1
    for i in range(1,k + 1):
        count[i]  = count[i] + count[i - 1]
        # count[i] += count[i - 1]
    for i in range(n - 1,-1,-1):
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
    for i in range(0,n):
        array[i] = output[i]

"""