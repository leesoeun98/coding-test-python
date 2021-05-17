"""import sys
card=[]
for _ in range(int(input())):
    card.append(int(sys.stdin.readline()))
card.sort()
before=card[0]
answer=[]
cnt=0
for i in range(len(card)):
    if card[i]==before:
        cnt+=1
    else:
        answer.append((before, cnt))
        before=card[i]
        cnt=0
        cnt+=1
answer.append((before, cnt))
answer.sort(key=lambda x:(-x[1], x[0]))
print(answer)
print(answer[0][0])"""
dic={}
for _ in range(int(input())):
    num=int(input())
    if num in dic:
        dic[num]+=1
    else:
        dic[num]=1
dic=sorted(dic.items(), key=lambda x:(-x[1], x[0]))
print(dic[0][0])
