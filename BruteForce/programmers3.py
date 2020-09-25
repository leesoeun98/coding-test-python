def solution(brown, yellow):
    for yellow_height in range(1, yellow+1):
        #yellow 타일의 개수를 이용해 가로, 세로를 구한다.
        if yellow % yellow_height==0:
            yellow_width=yellow//yellow_height
            if brown==(yellow_width)*2+2*(2+yellow_height):
                #yellow타일의 가로, 세로 개수로 갈색 타일의 개수를 구해보고 그것이 brown과 맞으면 해당 가로, 세로를 반환한다.
                return [yellow_width+2, yellow_height+2]