n = int(input())
arr = list(map(int, input().split()))
freq = {}
for x in arr:
    freq[x] = freq.get(x, 0) + 1
max_freq = max(freq.values())
answer = min(x for x in freq if freq[x] == max_freq)
print(answer)