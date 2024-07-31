N = int(input())
nums = list(map(int, input().split()))

# 같은 숫자로 만들기
num_count = {}
for num in nums:
    if num in num_count:
        num_count[num] += 1
    else:
        num_count[num] = 1
same_number_changes = N - max(num_count.values())

# 일정한 차이로 만드는 경우
min_changes = N - 1  # 모든 숫자가 다르다고 가정하고 시작
for i in range(N):
    for j in range(i + 1, N):
        if (nums[j] - nums[i]) % (j - i) == 0:
            d = (nums[j] - nums[i]) // (j - i)
            count = 0
            for k in range(N):
                if nums[k] != nums[i] + d * (k - i):
                    count += 1
            min_changes = min(min_changes, count)

# 최종 답
answer = min(same_number_changes, min_changes)
print(answer)