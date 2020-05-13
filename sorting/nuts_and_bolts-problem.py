def partition_modified(array,low,high,pivot):
    i = low 
    for j in range(low,high):
        if array[j] <= pivot:
            (array[i],array[j]) = (array[j],array[i])
            i += 1
        elif array[j] == pivot:
            (array[j],array[high]) = (array[high],array[j])
            j -= 1
    (array[i + 1],array[high]) = (array[high],array[i + 1])

    return i 

def nuts_and_bolts(nuts,bolts,low,high):
    if low < high:
        pivot_lock = partition_modified(nuts,low,high,bolts[high])
        partition_modified(bolts,low,high,nuts[pivot_lock])
        nuts_and_bolts(nuts,bolts,low,pivot_lock - 1)
        nuts_and_bolts(nuts,bolts,pivot_lock + 1,high)

"""
Input : nuts[] = {'@', '#', '$', '%', '^', '&'}
        bolts[] = {'$', '%', '&', '^', '@', '#'}
Output : Matched nuts and bolts are-
        $ % & ^ @ # 
        $ % & ^ @ #  
"""
# %%
nuts = ['@', '#', '$', '%', '^', '&']
bolts = ['$', '%', '&', '^', '@', '#']
n_d = dict()
for i in nuts:
    n_d[i] = True
for i in bolts:
    if n_d[i] == True:
        n_d[i] = i


