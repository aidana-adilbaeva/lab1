def cond(x):
    if x % 2 == 0:
        return True
    else:
        return False

n = int(input())
a = list(map(int, input().split()))

res = list(filter(cond, a))

print(len(res))