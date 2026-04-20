import re

s = input()
x = r"\d{2}/\d{2}/\d{4}"
arr = re.findall(x, s)
print(len(arr))