n = int(input())
a = list(map(int, input().split()))

x = sorted(set(a))
print(*x)