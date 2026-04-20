#squares from A to B
def squares(m, n):
    for i in range(m, n + 1):
            yield i*i

m, n = map(int, input().split())
x = squares(m, n)
for i in x:
    print(i)