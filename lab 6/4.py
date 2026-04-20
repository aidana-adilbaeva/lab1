x = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
res = [x * y for x, y in zip(a, b)]
print(sum(res))

