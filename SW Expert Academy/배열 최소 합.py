T = int(input())

def abc(level, sum):
    global minSum
    if sum > minSum: return
    if level == n:
        if sum < minSum:
            minSum = sum
        return
    for i in range(len(nums)):
        if used[i] == 0:
            used[i] = 1
            path[level] = nums[i]
            abc(level+1, sum + lst[level][nums[i]])
            used[i] = 0

for tc in range(1, T+1):
    n = int(input())
    lst = []
    for i in range(n):
        lst.append(list(map(int, input().split())))
    nums = [i for i in range(n)]
    path = [0]*n
    used = [0]*len(nums)
    minSum = 21e8
    abc(0, 0)
    print(f"#{tc} {minSum}")
