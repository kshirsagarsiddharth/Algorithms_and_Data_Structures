def insertion_sort_util(array):
    for step in range(len(array)):
        key = array[step]
        j = step - 1

        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j-= 1

        array[j + 1] = key
    
    return array

def bucket_sort(array):
    bucket = []

    # create empty buckets
    for i in range(len(array)):
        bucket.append([])
    # insert the elements into their respective buckets
    for j in array:
        index_b = int(10 * j)
        bucket[index_b].append(j)
    
    # sort the elements of each bucket
    for i in range(len(array)):
        bucket[i] = insertion_sort_util(bucket[i])

    # get the sorted elements
    k = 0
    for i in range(len(array)):
        for j in range(len(bucket[i])):
            array[k] = bucket[i][j]
            k += 1
    return array

array = [.42, .32, .33, .52, .37, .47, .51]
bucket_sort(array)
print(array)