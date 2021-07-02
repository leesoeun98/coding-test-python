plain = input()
code = []
for p in plain:
    if p.isdigit():
        code.append(p)
    elif p.isspace():
        code.append(p)
    else:
        if p.islower():
            if ord(p) + 13 <= ord('z'):
                code.append(chr((ord(p)+13)))
            else:
                code.append(chr((ord(p) - 13)))
        else:
            if ord(p)+13<=ord('Z'):
                code.append(chr((ord(p)+13)))
            else:
                code.append(chr((ord(p)-13)))
print(''.join(code))

"""
code=input()
new=[]
for c in code:
    if c.islower():
        n=chr(((ord(c)-ord('a')+13)%26)+ord('a'))
    elif c.isupper():
        n=chr(((ord(c)-ord('A')+13)%26)+ord('A'))
    else:
        n=c
    new.append(n)
print(''.join(new))
"""