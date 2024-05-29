N, M = map(int, input().split())
nums = list(map(int, input().split()))
answer = 0
current_sum = 0
start = 0

for end in range(N):
    current_sum += nums[end]

    while current_sum > M and start <= end:
        current_sum -= nums[start]
        start += 1

    if current_sum == M:
        answer += 1

print(answer)
