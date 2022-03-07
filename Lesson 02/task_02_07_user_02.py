import sys
def primes():
    for i in range(2, sys.maxsize):
        if len(list(filter(lambda n: i%n == 0, range(2, i)))) == 0:
            yield i

# n = 10**4 Elapsed time: 16.590 sec