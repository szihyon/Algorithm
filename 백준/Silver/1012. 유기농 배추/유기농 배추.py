from collections import deque

def bfs(stY, stX):
    q = deque()
    q.append((stY, stX))
    directY = [-1, 0, 0, 1]
    directX = [0, -1, 1, 0]

    while q:
        nowY, nowX = q.popleft()
        for i in range(4):
            dy = directY[i] + nowY
            dx = directX[i] + nowX
            if dy < 0 or dx < 0 or dy > n-1 or dx > m-1: continue
            if lst[dy][dx] == 0: continue
            lst[dy][dx] = 0
            q.append((dy, dx))
    return

T = int(input())
for _ in range(T):
    m, n, k = map(int, input().split())
    lst = [[0]*m for _ in range(n)]
    for i in range(k):
        x, y = map(int, input().split())
        lst[y][x] = 1
    cnt = 0
    for i in range(n):
        for j in range(m):
            if lst[i][j] == 1:
                cnt += 1
                bfs(i, j)
    print(cnt)