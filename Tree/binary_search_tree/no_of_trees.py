def count_trees(n):
    if n<= 1:
        return 1
    else:
        sum = 0
        for root in range(1,n + 1):
            left = count_trees(root - 1)
            right = count_trees(n - root)

            sum += left * right