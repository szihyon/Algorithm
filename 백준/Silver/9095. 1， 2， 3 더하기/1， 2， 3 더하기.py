# https://www.acmicpc.net/problem/9095

T = int(input())
nums = [1, 2, 3]

def dfs(sumV):
    global answer, n
    if sumV > n:
        return
    if sumV == n:
        answer += 1
        return
    for i in range(3):
        dfs(sumV+nums[i])

for _ in range(T):
    n = int(input())
    answer = 0
    dfs(0)
    print(answer)