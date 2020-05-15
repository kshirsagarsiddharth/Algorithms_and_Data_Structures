def print_duplicates_hash(array):
    dic = {}
    for i in array:
        try:
            dic[i] += 1
        except:
            dic[i] = 1
    
    for item in dic:
        if dic[item] > 1:
            print(item)

array = [12, 11, 40, 12,5, 6, 5, 12, 11] 
print_duplicates_hash(array)

def print_duplicates_space_efficient(array):
    for i in range(array):
        if array[abs(array[i])] > 0:
            array[abs(array[i])] = - array[abs(array[i])]
        else:
            print(abs(array[i]),end = " ")
