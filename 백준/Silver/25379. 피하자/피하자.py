N = int(input())
nums = list(map(int, input().split()))
cnt = 0

# 홀수와 짝수가 인접한 경우 세기
def count(nums):
    global cnt
    cnt = 0
    for i in range(N-1):
        if nums[i] % 2 != nums[i+1] % 2:
            cnt += 1
            
count(nums) # 처음 배열에 대해 카운트

# 인접한 경우가 2개 이상인 경우,
# 홀수와 짝수가 인접한 경우가 한 번이 될 때까지 원소 교환
answer = 0
while cnt > 1:
    for i in range(N - 1):
        if nums[i] % 2 != nums[i + 1] % 2:
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
            answer += 1 # 교환한 횟수 + 1
            count(nums) # 교환 후 홀수와 짝수가 인접한 경우 세기
            if cnt == 1: # 인접한 경우가 한 번이 되면 반복문 종료
                break

# 정답 출력
print(answer)