import re

s = input()
if re.search(r'dog|cat', s):
    print("Yes")
else:    print("No")