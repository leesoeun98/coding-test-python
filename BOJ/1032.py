files=[]
n=int(input())
for _ in range(n):
    files.append(input())
check=['?' for i in range(len(files[0]))]
if n==1:
    print(''.join(files))
else:
    for j in range(len(files[0])):
        for i in range(n-1):
            if files[i][j]!=files[i+1][j]:
                check[j]='?'
                break
        else:
            check[j]=files[i][j]
    print(''.join(check))