import re

s = input()
x = r"Name: (.+), Age: (.+)"
match = re.search(x, s)
print(match.group(1), match.group(2))