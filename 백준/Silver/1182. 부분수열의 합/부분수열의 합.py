n, s = map(int, input().split())
nums = list(map(int, input().split()))

def dfs(start, level, sm):
    global cnt
    if level > 0 and sm == s:
        cnt += 1

    if level == n:
        return

    for i in range(start, len(nums)):
        dfs(i+1, level+1, sm+nums[i])

cnt = 0
dfs(0, 0, 0)
print(cnt)
