import re

s = input()
x = r"\b\w+\b"
string = re.compile(x)
arr = string.findall(s)
print(
    len(arr)
)