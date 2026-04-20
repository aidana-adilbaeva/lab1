import re

s = input()
if re.match("^[a-zA-Z].*[0-9]$", s):
    print("Yes")
else: 
       print("No")    