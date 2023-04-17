from collections import deque

n, m = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]

def bfs(stY, stX):
    directY = [-1, 0, 0, 1]
    directX = [0, -1, 1, 0]
    q = deque()
    q.append((stY, stX))
    area = 0
    lst[stY][stX] = 0
    area += 1

    while q:
        nowY, nowX = q.popleft()
        for i in range(4):
            dy = directY[i] + nowY
            dx = directX[i] + nowX
            if dy < 0 or dx < 0 or dy > n-1 or dx > m-1: continue
            if lst[dy][dx] == 1:
                q.append((dy, dx))
                lst[dy][dx] = 0
                area += 1
    return area


cnt = 0
Max = 0
for i in range(n):
    for j in range(m):
        if lst[i][j] == 1:
            cnt += 1
            res = bfs(i, j)
            if res > Max:
                Max = res


print(cnt)
print(Max)

