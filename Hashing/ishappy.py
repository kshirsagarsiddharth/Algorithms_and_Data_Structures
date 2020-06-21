def isHappy(n):
    hashset = set()
    while n != 1:
        n = sum([int(i) ** 2 for i in str(n)])
        if n in hashset:
            return False
        else:
            hashset.add(n)
    return True