n = int(input())
arr = list(map(int, input().split()))
arr2 = []
for x in arr:
    if x not in arr2: 
        print("YES") 
        arr2.append(x)
    else: print("NO")