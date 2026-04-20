def to_int(word):
    if word == 'ONE':
        return '1'
    elif word == 'TWO':
        return '2'
    elif word == 'THR':
        return '3'
    elif word == 'FOU':
        return '4'
    elif word == 'FIV':
        return '5'
    elif word == 'SIX':
        return '6'
    elif word == 'SEV':
        return '7'
    elif word == 'EIG':
        return '8'
    elif word == 'NIN':
        return '9'
    elif word == 'ZER':
        return '0'
def to_str(word):
    if word == '1':
        return 'ONE'
    elif word == '2':
        return 'TWO'
    elif word == '3':
        return 'THR'
    elif word == '4':
        return 'FOU'
    elif word == '5':
        return 'FIV'
    elif word == '6':
        return 'SIX'
    elif word == '7':
        return 'SEV'
    elif word == '8':
        return 'EIG'
    elif word == '9':
        return 'NIN'
    elif word == '0':
        return 'ZER'    
    
num = input()
op = ""
for i in "+-*":
    if i in num:
        op = i
        a, b = num.split(i)
a2 = ""
b2 = ""            
for i in range(0, len(a),3):
    a2 += to_int(a[i:i+3])            

for i in range(0, len(b),3):
    b2 += to_int(b[i:i+3])
res = 0
if op == "+":
    res = int(a2) + int(b2)
elif op == "-":
    res = int(a2) - int(b2)
elif op == "*":
    res = int(a2) * int(b2)

for x in str(res):
    print(to_str(x),end="")
    
    