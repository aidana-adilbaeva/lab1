x = int(input())
s = list(map(str, input().split()))

for i, j in enumerate(s):
    print(f"{i}:{j} ", end=" ")