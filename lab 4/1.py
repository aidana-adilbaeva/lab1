#squares of numbers
def square(n):
    for i in range(1,n+1):
        yield i*i
n = int(input())  
x = square(n)
for i in range(n): 
    print(next(x))  