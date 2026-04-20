x = int(input())
nums = input().split()
sum = 0
for i in range(x):
    if int(nums[i]) > 0:
        sum += 1
print(sum)