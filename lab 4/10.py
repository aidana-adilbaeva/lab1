#limited cycle
def limited_cycle(lst, k):
    for _ in range(k):
        for item in lst:
            yield item

lst = input().split()
k = int(input())

for x in limited_cycle(lst, k):
    print(x, end=' ')