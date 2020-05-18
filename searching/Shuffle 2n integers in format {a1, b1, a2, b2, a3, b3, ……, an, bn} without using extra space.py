def shuffle_elements_bruteforce(array,n):
    i = 0
    q = 1
    k = n

    while i < n:
        j = k

        while j > i + q:
            array[j - 1],array[j] = array[j],array[j - 1]
            j -= 1
        i += 1 
        q += 1
        k += 1
                                                                        