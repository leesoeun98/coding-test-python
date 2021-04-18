n = int(input())
word=dict()
for _ in range(n):
    w=input()
    #default는 0으로 지정
    word[w]=word.get(w, 0)+1
for _ in range(n-1):
    d=input()
    word[d] = word.get(d, 0) - 1
for key, value in word.items():
    if value!=0:
        print(key)
        break
