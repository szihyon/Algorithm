N = int(input())
nums = list(map(int, input().split()))

num_dict = {}
for num in nums:
    if num in num_dict:
        num_dict[num] += 1
    else:
        num_dict[num] = 1

# 모든 수를 같은 수로 만들 때의 최소 변경 횟수
same_number_changes = N - max(num_dict.values())

# 일정한 차이로 증가/감소하는 수열을 만들 때의 최소 변경 횟수
min_diff_changes = float('inf')
for i in range(N):
    for j in range(i + 1, N):
        d = nums[j] - nums[i]
        count = 0
        for k in range(N):
            expected_value = nums[i] + d * (k - i)
            if nums[k] != expected_value:
                count += 1
        min_diff_changes = min(min_diff_changes, count)

# 정답은 두 경우 중 최소값
answer = min(same_number_changes, min_diff_changes)
print(answer)