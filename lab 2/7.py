x = int(input())
a = input().split() 
y = -9999999999
z = 0
for i in range(x):
   if int(a[i]) > y:
       y = int(a[i])
       z = i
print(z+1)  