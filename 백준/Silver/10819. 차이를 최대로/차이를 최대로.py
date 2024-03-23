N = int(input())
nums = list(map(int, input().split()))
com_lst = [0] * N
used = [0] * N
maxV = 0
def dfs(level):
    global maxV
    if level == N:
        sumV = 0
        for k in range(N-1):
            sumV += abs(com_lst[k] - com_lst[k+1])
        if sumV > maxV:
            maxV = sumV
        return
    for i in range(N):
        if used[i] == 1: continue
        used[i] = 1
        com_lst[level] = nums[i]
        dfs(level+1)
        used[i] = 0

dfs(0)
print(maxV)