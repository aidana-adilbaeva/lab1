s = input()
z = 0

for i in s:
    if int(i) % 2 == 0:
        z += 1

print("Valid" if z == len(s) else "Not valid")