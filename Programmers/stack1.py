def solution(prices):
    answer = []
    #1. 앞부터 비교위해 현재값 pop
    #2. 각 주식가격과 current_price 비교 (어차피 prices에 current_price없어서 current_price뒤부터 비교됨)
    while len(prices)>0:
        current_price=prices.pop(0)
        time=0
        for price in prices:
            time+=1
            if current_price>price:
                break
        answer.append(time)
    return answer

print(solution([1,2,3,2,3]))