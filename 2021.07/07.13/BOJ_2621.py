cards=[]
for _ in range(5):
    cards.append(list(input().split()))
color_flag = True
before_color=cards[0][0]
for color, num in cards:
    if color!=before_color:
        color_flag=False
        break

