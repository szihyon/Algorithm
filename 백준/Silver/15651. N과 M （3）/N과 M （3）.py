n, m = map(int, input().split())
nums = [i for i in range(1, n+1)]

def abc(level):
    if level == m:
        for i in range(len(path)):
            print(path[i], end=' ')
        print()
        return
    for j in range(len(nums)):
        path[level] = nums[j]
        abc(level+1)

path = [0]*m
abc(0)