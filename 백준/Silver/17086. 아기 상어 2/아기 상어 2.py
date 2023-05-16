from collections import deque

n, m = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]


def bfs(stY, stX, cnt):
    q = deque()
    q.append((stY, stX, cnt))
    directY = [-1, -1, -1, 0, 0, 1, 1, 1]
    directX = [-1, 0, 1, -1, 1, -1, 0, 1]
    visit = [[0] * m for _ in range(n)]

    while q:
        nowY, nowX, cnt = q.popleft()
        if lst[nowY][nowX] == 1:
            return cnt

        for i in range(8):
            dy = directY[i] + nowY
            dx = directX[i] + nowX
            if dy < 0 or dx < 0 or dy > n-1 or dx > m-1: continue
            if visit[dy][dx] == 0:
                visit[dy][dx] = 1
                q.append((dy, dx, cnt + 1))

ans = 0
for i in range(n):
    for j in range(m):
        res = bfs(i, j, 0)
        if res > ans:
            ans = res

print(ans)