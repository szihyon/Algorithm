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
        if level > 0 and path[level-1] > nums[j]:continue
        path[level] = nums[j]
        abc(level+1)

path = [0]*m
dic = dict()
abc(0)
