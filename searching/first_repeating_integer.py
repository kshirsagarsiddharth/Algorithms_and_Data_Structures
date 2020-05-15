def first_repeating_element(array,n):
    dic = {}
    Min = -1

    for i in range(n - 1,-1,-1):
        if array[i] in dic.keys():
            Min = i
        else:
            dic[i] = 1

    if Min == -1:
        print("There are no repeating elements")
    else:
        print("The repearing element is {}".format(array[Min]))
         