#powers of 2 generator
def powers(n):
    for i in range(0, n+1):
        yield 2**i

n = int(input())
for p in powers(n):
    print(p, end=' ')