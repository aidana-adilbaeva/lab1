import re

s = input()
x = re.compile(r'^\d+$')
p = x.search(s)
if p:
    print("Match")
else:    print("No match")