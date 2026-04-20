import re

s = input()
n = input()
m = input()
s = re.sub(n, m, s)
print(s)