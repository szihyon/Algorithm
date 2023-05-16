from collections import deque

m, n = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]

def bfs():
    directY = [-1, 0, 0, 1]
    directX = [0, -1, 1, 0]
    while q:
        nowY, nowX, day = q.popleft()
        for i in range(4):
            dy = directY[i] + nowY
            dx = directX[i] + nowX
            if dy < 0 or dx < 0 or dy > n-1 or dx > m-1: continue
            if lst[dy][dx] == 0:
                lst[dy][dx] = 1
                q.append((dy, dx, day+1))
    return day

q = deque()
for i in range(n):
    for j in range(m):
        if lst[i][j] == 1:
           q.append((i, j, 0))

if q:
    res = bfs()

cnt = 0
for i in range(n):
    for j in range(m):
       if lst[i][j] == 0:
           cnt += 1

if cnt > 0:
    print(-1)
else:
    print(res)