from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])

    q = deque()
    q.append([0, 0, 1])
    visit = [[0]*m for _ in range(n)]
    visit[0][0] = 1
    
    directY = [-1, 1, 0, 0]
    directX = [0, 0, -1, 1]
    
    while q:
        nowY, nowX, cnt = q.popleft()
        if nowY == n-1 and nowX == m-1:
            return cnt
        for i in range(4):
            dy = nowY + directY[i]
            dx = nowX + directX[i]
            if dy > n-1 or dx > m-1 or dy < 0 or dx < 0:continue
            if maps[dy][dx] == 0 : continue 
            if visit[dy][dx] == 1 : continue
            visit[dy][dx] = 1
            q.append((dy, dx, cnt+1))
    return -1