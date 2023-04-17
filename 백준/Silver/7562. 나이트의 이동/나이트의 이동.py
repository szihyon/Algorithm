from collections import deque

def bfs(stY, stX, cnt):
    q = deque()
    q.append((stY, stX, cnt))
    directY = [-2, -2, -1, -1, 1, 1, 2, 2]
    directX = [-1, 1, -2, 2, -2, 2, -1, 1]

    while q:
        nowY, nowX, cnt = q.popleft()
        if nowY == edY and nowX == edX:
            return cnt
        for i in range(8):
            dy = directY[i] + nowY
            dx = directX[i] + nowX
            if dy < 0 or dx < 0 or dx > n-1 or dy > n-1:continue
            if used[dy][dx] == 1: continue
            used[dy][dx] = 1
            q.append((dy, dx, cnt+1))

t = int(input())

for _ in range(t):
    n = int(input())
    lst = [[0]*n for _ in range(n)]
    stY, stX = map(int, input().split())
    edY, edX = map(int, input().split())
    used = [[0]*n for _ in range(n)]
    used[stY][stX] = 1
    print(bfs(stY, stX, 0))