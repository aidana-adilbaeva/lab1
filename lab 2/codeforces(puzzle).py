def puzzle(n):
    while n % 2 == 0:
        n //= 2
        if n == 1:
            print("YES")
        else:
            print("NO")

for i in range(int(input())):   
    n = int(input())
    puzzle(n)         
