import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
lst = [[0] * n for _ in range(n)]
for _ in range(m):
    p1, p2 = map(int, input().split())
    lst[p1 - 1][p2 - 1] = 1
    lst[p2 - 1][p1 - 1] = 1

visit = [0] * n

def dfs(now):
    visit[now] = 1

    for i in range(n):
        if lst[now][i] == 1 and visit[i] == 0:
            dfs(i)

cnt = 0

for i in range(n):
    if visit[i] == 0:
        cnt += 1
        dfs(i)

print(cnt)