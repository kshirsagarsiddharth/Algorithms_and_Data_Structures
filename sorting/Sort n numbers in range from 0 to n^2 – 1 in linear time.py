def counting_sort(array,n,exp):
    output = [0] * n
    count = [0] * n

    for i in range(n):
        count[i] = 0

    # store count of occurances
    for i in range(n):
        count[(array[i] // exp) % n] += 1

    for i in range(1,n):
        count[(array[i] // exp) % n] += 1

    for i in range(n - 1,-1,-1):
        output[count[(array[i] // exp) % n] - 1] = array[i]
        count[(array[i] // exp) % n] -= 1
    
    for i in range(n):
        array[i] = output[i]

def sort(array,n):
    counting_sort(array,n,1)
    counting_sort(array,n,n)