def search(matrix,n,x):
    j = n - 1
    i = 0

    while i < n and j > 0 :
        if matrix[i][j] == x:
            print("The element is at position {} and {}".format(i,j))
        
        if matrix[i][j] > x:
            j -= 1
        else:
            i += 1

