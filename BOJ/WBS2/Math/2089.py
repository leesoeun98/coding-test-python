n = int(input())
res = ""
if not n:
    print('0')
    exit()
else:
    # 더하는 순서가 매우 중요 1+res이냐 res+1이냐 차이 구분 하기
    while n:
        # 나머지가 1일때
        if n % -2:
            res = '1' + res
            n = n // -2 + 1
        # 나머지가 0일 때
        else:
            res = '0' + res
            n = n // -2
    print(res)
