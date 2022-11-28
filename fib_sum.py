import time

n = 10


def fib_iterative(n):
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
    return a


start_time = time.time()
print("Fibonacci numbers to sum: %i" % fib_iterative(n))
fib_iterative(n)
print("Time: %f" % (time.time() - start_time))

n = 100


def fib_iterative(n):
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
    return a


start_time = time.time()
print("Fibonacci numbers to sum: %i" % fib_iterative(n))
fib_iterative(n)
print("Time: %f" % (time.time() - start_time))

n = 1000


def fib_iterative(n):
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
    return a


start_time = time.time()
print("Fibonacci numbers to sum: %i" % fib_iterative(n))
fib_iterative(n)
print("Time: %f" % (time.time() - start_time))

n = 10000


def fib_iterative(n):
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
    return a


start_time = time.time()
print("Fibonacci numbers to sum: %i" % fib_iterative(n))
fib_iterative(n)
print("Time: %f" % (time.time() - start_time))

n = 100000


def fib_iterative(n):
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
    return a


start_time = time.time()
print("Fibonacci numbers to sum: %i" % fib_iterative(n))
fib_iterative(n)
print("Time: %f" % (time.time() - start_time))

