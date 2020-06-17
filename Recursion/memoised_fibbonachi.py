def memoised_fibbonachi(N):
    cache = {}
    def fib_rec(N):
        if N in cache:
            return cache[N]
        if N < 2:
            result = N
        else:
            result = fib_rec(N - 1) + fib_rec(N - 2)
        cache[N] = result

        return result