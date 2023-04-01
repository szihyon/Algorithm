n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

def abc(level):
    if level == m:
        print(*path)
        return

    for j in range(len(nums)):
        if used[j] == 1: continue
        if level > 0 and nums[j] < path[level-1]: continue
        used[j] = 1
        path[level] = nums[j]
        abc(level+1)
        used[j] = 0

path = [0]*m
used = [0]*n
abc(0)