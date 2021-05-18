st = list(input())
alphabet=[-1]*26
for idx, s in enumerate(st):
    if alphabet[ord(s)-ord('a')]==-1:
        alphabet[ord(s) - ord('a')]=idx
print(*alphabet)