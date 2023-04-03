n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

def abc(level):
    if level == m:
        num = ' '.join(map(str, path))
        if num not in dic:
            dic[num] = 1
            print(num)
        return

    for j in range(len(nums)):
        if used[j] == 1:continue
        if level > 0 and path[level-1] > nums[j]:continue
        used[j] = 1
        path[level] = nums[j]
        abc(level+1)
        used[j] = 0

path = [0]*m
used = [0]*n
dic = dict()
abc(0)