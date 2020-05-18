def find_triplets_hashing(array,n):
    s = set()
    for i in range(0,n - 1):
        for j in range(i + 1,n):
            pass


def find_triplets_dual_pointers(array,k,size):
    array.sort()
    min_l = 0
    min_r = 0
    for i in range(0,size - 2):
        left = i
        right = len(array) - 1

        while left < right:

            if array[left] + array[right] + array[i] == k:
                min_l = left
                min_r = right
                print(array[min_l],array[min_r],array[i])
                return 1

            elif array[left] + array[right] + array[i] > k:
                right -= 1

            else:
                left -= 1 
    return 0

def find_triplets_bruteforce(array,Sum,size):
    for i in range(0,size - 2):

        for j in range(i + 1,size - 1):

            for k in range(j + 1,size):

                if array[i] + array[j] + array[k] == Sum:
                    return 1
    return 0

def find_triplets_hashing(array,Sum,size):
    for i in range(0,size - 1):
        s = set()
        curr_sum = Sum - array[i]
        for j in range(i + 1,size):
            if curr_sum - array[j] in s:
                print(array[i],array[j],curr_sum - array[j])
                return True
            s.add(array[j])
        
