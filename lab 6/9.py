n = int(input())
a = list(map(str, input().split()))
b = list(map(str, input().split()))

res = list(zip(a, b))
x = input()

if x in a:
    for i, j in res:
        if i == x:
            print(j)   
else:   print("Not found")             