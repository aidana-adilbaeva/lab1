x = int(input())
arr = []
for i in range(x):
    arr.append(input())

arr2 = []
answer = 0

for i in arr:
    if i not in arr2:
        if arr.count(i) == 3:
            answer += 1
        arr2.append(i)

print(answer)
