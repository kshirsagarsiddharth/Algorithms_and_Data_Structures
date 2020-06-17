"""
climb stairs recursively with brute force
"""
def climb_recursive(n,i = 0):
    if i > n:
        return 0
    if i == n:
        return 1
    return climb_recursive(n,i + 1) + climb_recursive(n,i + 2)
cache = {}
def climb_stairs_memiozed(n,i = 0):
    if i > n:
        return 0
    if i == n:
        return 1
    if i in cache:
        return cache[i]
    cache[i] = climb_stairs_memiozed(n, i + 1) + climb_stairs_memiozed(n,i + 2)
    return cache[i]