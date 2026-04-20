import re

s = input()
def second(x):
    d = x.group()
    return d * 2   

first = r"\d"
res = re.sub(first, second, s)
print(res)     