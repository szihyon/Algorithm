n, m = map(int, input().split())
nums = [i for i in range(1, n+1)]

def abc(level, start):
    if level == m:
        for i in range(len(path)):
            print(path[i], end=' ')
        print()
        return
    for j in range(start, len(nums)):
        if used[j] == 1: continue
        used[j] = 1
        path[level] = nums[j]
        abc(level+1, j+1)
        used[j] = 0

path = [0]*m
used = [0]*n
abc(0, 0)