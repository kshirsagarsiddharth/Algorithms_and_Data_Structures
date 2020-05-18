def search_in_a_matrix(matrix,x,n):
    i = 0
    j = n - 1

    while i < n and j >= 0:

        if matrix[i][j] == x:
            return (i,j)
        
        if matrix[i][j] > x:
            j -= 1
        
        if matrix[i][j] < x:
            i += 1
    return False

mat = [ [10, 20, 30, 40], 
        [15, 25, 35, 45], 
        [27, 29, 37, 48], 
        [32, 33, 39, 50] ] 
print(search_in_a_matrix(mat, 29,4))

