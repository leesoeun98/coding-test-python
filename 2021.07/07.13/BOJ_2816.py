n=int(input())
channel=[]
for i in range(n):
    name=input()
    if name=='KBS1':
        kbs1=i
    if name=='KBS2':
        kbs2=i
    channel.append(name)

ans=""
ans+='1'*kbs1
ans+='4'*kbs1
if kbs1>kbs2:
    kbs2+=1
ans+='1'*kbs2
ans+='4'*(kbs2-1)
print(ans)

