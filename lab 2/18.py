n = int(input())
arr = []
for i in range(n):
    arr.append(input())
arr2 = []
for x in arr:
    if x not in arr2:
        arr2.append(x)
arr2.sort()
for s in arr2:
    first_index = arr.index(s) + 1 
    print(s, first_index)