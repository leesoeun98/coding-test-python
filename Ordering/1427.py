numstring=input()
# 숫자 배열을 자릿수대로 나누는 것은 문자열로 생각하자
#문자열을 내림차순으로 정렬
numstring=sorted(numstring, reverse=True)

# 배열 원소 합쳐서 출력은 join
print("".join(numstring))