def nonzero(x):
    return x != 0

n = int(input())
a = list(map(int, input().split()))

res = list(map(nonzero, a))
print(sum(res))

