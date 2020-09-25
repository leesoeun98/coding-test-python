def solution(brown, yellow):
    for yellow_height in range(1, yellow+1):
        if yellow % yellow_height==0:
            yellow_width=yellow//yellow_height
            if brown==(yellow_width)*2+2*(2+yellow_height):
                return [yellow_width+2, yellow_height+2]