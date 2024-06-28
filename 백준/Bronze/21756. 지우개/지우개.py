# 홀수번 1, 3, 5 지우기 -> 왼쪽으로 모으기
N = int(input())
nums = [(i+1) for i in range(N)]

for i in range(N//2):
    temp = []
    n = len(nums)
    if n <= 1: break
    for k in range(n//2):
        # nums[2*k+1]만 남기기 or nums[2*k+2]만 지우기
        temp.append(nums[2*k+1])
    nums = temp

print(nums[0])