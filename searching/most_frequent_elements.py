# efficient most frequent elements solution

def most_frequent_elements(array,n):
    Max = 0
    count = 0
    for i in range(0,n):
        array[array[i] % n] += n
    for i in range(0,n):
        if array[i] > Max:
            Max = array[i]
            count = i
            array[i] = array[i] % n
    
    return array[count]
    

arr = [1, 2, 2, 2, 2, 3, 4, 7 ,8 ,8] 
n = len(arr) 
print(most_frequent_elements(arr,n))