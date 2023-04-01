n, m = map(int, input().split())
nums = [i for i in range(1, n+1)]

def abc(level):
    if level == m:
        print(*path)
        return

    for j in range(len(nums)):
        if level > 0 and nums[j] < path[level-1]: continue
        path[level] = nums[j]
        abc(level+1)

path = [0]*m
lst = []
abc(0)