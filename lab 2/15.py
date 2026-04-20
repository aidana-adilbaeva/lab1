n = int(input())
arr = []
for i in range(n):
    arr.append(input())
freq = {}
for x in arr:
    freq[x] = freq.get(x, 0) + 1
print(len(freq))
