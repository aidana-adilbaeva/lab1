def sum(n,m,l):
    if n + m == l or n + l == m or m + l == n:
        return "Yes"
    else:      
        return "No"

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    print(sum(a,b,c))