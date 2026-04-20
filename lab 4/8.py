#prime numbers range
def primes(n):
    for i in range(2, n+1):
        if all(i % j != 0 for j in range(2, i)):
            yield i

n = int(input())
for p in primes(n):
    print(p, end=' ')