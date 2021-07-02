num, base = input().split()
res=0
for i in range(len(num)-1, -1, -1):
    digit=0
    if ord(num[i])>=ord('A'):
        digit=ord(num[i])-ord('A')+10
    else:
        digit=int(num[i])
    res+=digit*pow(int(base), len(num)-i-1)
print(res)

"""
num, b = input().split()
res=0
for i in range(len(num)):
    digit=0
    if ord(num[i])>=ord('A'):
        digit=ord(num[i])-ord('A')+10
    else:
        digit=int(num[i])
    res=res*int(b)+digit
print(res)"""