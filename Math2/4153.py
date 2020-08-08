while True:
    length=list(map(int, input().split()))
    if length[0]==0 and length[1]==0 and length[2]==0:
        break
    maxl=max(length)
    #최대값만 제거하고 나머지로 삼각형 판별 가능
    if maxl in length:
        length.remove(maxl)
    #삼각형이 아닌것도 예외처리하기
    if maxl<length[0]+length[1] and maxl**2==length[0]**2+length[1]**2:
        print('right')
    else:
        print('wrong')