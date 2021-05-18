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
