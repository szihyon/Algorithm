def solution(nums):
    answer = 0
    mon = dict()
    n = len(nums)
    for i in range(n):
        if nums[i] not in mon:
            mon[nums[i]] = 1
        else:
            mon[nums[i]] += 1
    if n//2 < len(mon):
        answer = n//2
    else:
        answer = len(mon)
    return answer