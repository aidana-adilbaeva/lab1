import re

s = input()
p = input()

x = re.escape(p) 
arr = re.findall(x, s)
print(len(arr))