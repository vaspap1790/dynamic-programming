import timeit


def fib(n):
    if n == 0: return 1
    if n == 1: return 1
    return fib(n - 1) + fib(n - 2)


def fib_memoization(n, cache=None):
    if n == 0: return 1
    if n == 1: return 1

    if cache is None: cache = {}
    if n in cache: return cache[n]

    result = fib_memoization(n - 1, cache) + fib_memoization(n - 2, cache)
    cache[n] = result
    return result


def fib_bottom_up(n):
    f1 = 1
    f2 = 1
    for i in range(2, n + 1):
        f1, f2 = f2, f1 + f2
    return f2


print(fib(4))
print(fib_memoization(4))
print(fib_bottom_up(4))

print('fib(4):', timeit.timeit('fib(4)', number=1, globals=globals()))
print('fib(30):', timeit.timeit('fib(15)', number=1, globals=globals()))

print('fib_memoization(4):', timeit.timeit('fib_memoization(4)', number=1, globals=globals()))
print('fib_memoization(30):', timeit.timeit('fib_memoization(15)', number=1, globals=globals()))

print('fib_bottom_up(4):', timeit.timeit('fib_bottom_up(4)', number=1, globals=globals()))
print('fib_bottom_up(30):', timeit.timeit('fib_bottom_up(15)', number=1, globals=globals()))