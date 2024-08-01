import sys
input = sys.stdin.readline

# N: 수열의 길이, M: 합을 구해야 하는 구간의 수
N, M = map(int, input().split())

# nums: 수열의 각 원소를 저장하는 리스트 (0을 추가하여 인덱스를 맞춤)
nums = [0] + list(map(int, input().split()))

# sum_nums: 각 인덱스까지의 부분합을 저장하는 리스트
sum_nums = []
temp = 0

# 수열의 각 원소에 대해 부분합을 계산하여 sum_nums에 저장
for num in nums:
    temp += num
    sum_nums.append(temp)

# M개의 구간에 대해 합을 계산하여 출력
for _ in range(M):
    # i, j: 합을 구해야 하는 구간의 시작과 끝 인덱스
    i, j = map(int, input().split())
    # sum_nums[j] - sum_nums[i - 1]: i부터 j까지의 구간 합을 계산하여 출력
    print(sum_nums[j] - sum_nums[i - 1])
