def abc(level):
    if level == 6:
        print(*path)
        return
    for i in range(len(nums)):
        if used[i] == 1: continue
        if level > 0 and path[level-1] > nums[i]:continue
        used[i] = 1
        path[level] = nums[i]
        abc(level+1)
        used[i] = 0

while True:
    k, *nums = list(map(int, input().split()))
    if k == 0:
        break
    used = [0]*k
    path = [0]*6
    abc(0)
    print()