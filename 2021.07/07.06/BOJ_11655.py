word=list(map(str, input()))
res=[]
for w in word:
    if w.isupper():
        res.append(chr(ord('A')+(ord(w)-ord('A')+13)%26))
    elif w.islower():
        res.append(chr(ord('a')+(ord(w)-ord('a')+13)%26))
    else:
        res.append(w)
print(''.join(res))
