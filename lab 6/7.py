n = int(input())
a = list(map(str, input().split()))

x = max(a, key=len)
print(x)
