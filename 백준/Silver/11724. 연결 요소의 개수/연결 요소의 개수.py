n, m = map(int, input().split())
lst = [[0]*n for _ in range(n)]
for _ in range(m):
    p1, p2 = map(int, input().split())
    lst[p1-1][p2-1] = 1
    lst[p2-1][p1-1] = 1

visit = [0]*n

def dfs(now):
    for i in range(n):
        if lst[now][i] == 1:
            if visit[i] == 0:
                visit[i] = 1
                dfs(i)

cnt = 0

for j in range(n):
    # for j in range(n):
    #     if lst[i][j] == 1:
            if visit[j] == 0:
                visit[j] = 1
                cnt += 1
                dfs(j)

print(cnt)