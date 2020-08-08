num=int(input())
for _ in range(num):
    h, w, n=map(int, input().split())
    #예외처리 잘하기 h가 6이고 n이 6, 12, 18...일때
    if n%h==0:
        ww=n//h
        hh=h
    #나머지
    else:
        ww = n // h + 1
        hh = n % h
    #출력에서도 예외처리
    if ww<10:
        print(str(hh)+'0'+str(ww))
    else:
        print(str(hh) + str(ww))