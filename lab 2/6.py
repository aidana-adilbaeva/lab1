x = int(input())
a = input().split() 
y = -9999999999
for i in range(x):
   if int(a[i]) > y:
       y = int(a[i])
print(y)    