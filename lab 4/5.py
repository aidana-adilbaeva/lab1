#the countdown
def num(n):
    while n >= 0:
        yield n
        n -= 1
n = int(input())
x = num(n)
for i in x:
    print(i)