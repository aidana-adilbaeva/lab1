x = int(input())
a = input().split()
c = -9999999999
b = 9999999999
for i in range(x):
   if int(a[i]) > c:
       c = int(a[i])
   if int(a[i]) < b:
       b = int(a[i])
for j in range(x):
    if int(a[j]) == c:
       a[j] = b  
    print(a[j], end=' ')   