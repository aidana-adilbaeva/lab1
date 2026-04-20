x = int(input())
epi = {}
for _ in range(x):
    name, series = input().split()
    n = int(series)
    if name in epi:
        epi[name] += n
    else:
        epi[name] = n

for y in sorted(epi):
    print(y, epi[y])
