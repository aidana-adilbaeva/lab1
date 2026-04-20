x = int(input())
y = list(map(int, input().split()))

if all(i >= 0 for i in y):
    print("Yes")
else:   print("No")
