st = list(input())
alphabet=[0]*26
for s in st:
    alphabet[ord(s)-ord('a')]+=1
print(*alphabet)