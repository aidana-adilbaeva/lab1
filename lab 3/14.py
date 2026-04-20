n = int(input())
numbers = list(map(int, input().split()))
q = int(input())

for i in range(q):
    op = input().split()
    if op[0] == "add":
        a = int(op[1])
        numbers = list(map(lambda x: x + a, numbers))
    elif op[0] == "multiply":
        a = int(op[1])
        numbers = list(map(lambda x: x * a, numbers))
    elif op[0] == "power":
        a = int(op[1])
        numbers = list(map(lambda x: x**a, numbers))
    elif op[0] == "abs":
        numbers = list(map(lambda x: abs(x), numbers))

print(*numbers)