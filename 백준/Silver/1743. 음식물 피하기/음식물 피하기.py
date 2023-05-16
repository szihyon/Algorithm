from collections import deque

n, m, k = map(int, input().split())
lst = [[0]*m for _ in range(n)]

for _ in range(k):
    r, c = map(int, input().split())
    lst[r-1][c-1] = 1

def bfs(stY, stX):
    q = deque()
    q.append((stY, stX))
    directY = [-1, 0, 0, 1]
    directX = [0, -1, 1, 0]
    area = 0
    while q:
        nowY, nowX = q.popleft()
        for i in range(4):
            dy = directY[i] + nowY
            dx = directX[i] + nowX
            if dy < 0 or dx < 0 or dy > n-1 or dx > m-1: continue
            if lst[dy][dx] == 1:
                lst[dy][dx] = 0
                area += 1
                q.append((dy, dx))
    return area

maxV = 0
for i in range(n):
    for j in range(m):
        if lst[i][j] == 1:
            res = bfs(i, j)
            if res > maxV:
                maxV = res

print(maxV)

