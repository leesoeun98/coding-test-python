n = int(input())
nums = list(input().split())
answers=[]
for num in nums:
    answer=0
    for nu in num:
        answer+=int(nu)
    answers.append(answer)
for i in range(n):
    if answers[i]==max(answers):
        print(nums[i])
        break