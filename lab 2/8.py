x = int(input())
a = []
for i in range(0, x + 1):
    if 2 ** i < x + 1:
        a.append(2 ** i)
print(*a)                