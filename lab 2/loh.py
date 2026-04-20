import sys
input = sys.stdin.readline
n = int(input())
for _ in range(n):
    x = int(input())
    y = list(map(int, input().split()))
    l = 0
    r = 0
    z = 0
    for j in range(x):
        s = set()
        for i in range(j, x):
            s.add(y[i])
            k = (i - j + 1) - len(s)
            if k > z:
                z = k
                l = j
                r = i
    print(l + 1, r + 1)