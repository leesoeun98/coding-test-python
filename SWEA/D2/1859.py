for t in range(int(input())):
    # 뒤부터 탐색해서 더 큰 값이 나오면 더하고 아님 그대로
    n = int(input())
    num = list(map(int, input().split()))
    last = num[-1]
    total = 0
    cnt = 0
    partsum = 0
    # 뒤에서 두번째거 부터 거꾸로
    for n in num[-2::-1]:
        # 사야함
        if n < last:
            cnt += 1
            partsum += n
        # 팔기
        else:
            total += last * cnt - partsum
            last = n
            cnt = 0
            partsum = 0
    if cnt >= 1:
        total += last * cnt - partsum
    print("#" + str(t + 1) + " " + str(total))

