def square(x):
    return x * x

n = int(input())
a = list(map(int, input().split()))

res = list(map(square, a))

print(sum(res))