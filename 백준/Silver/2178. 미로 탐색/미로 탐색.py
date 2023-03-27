from collections import deque

n, m = map(int, input().split())
lst= []

for i in range(n):
    lst.append(list(map(int, input())))
    
def bfs(stY, stX, cnt):
    directY = [-1, 0, 0, 1]
    directX = [0, 1, -1, 0]
    q = deque()
    q.append((stY, stX, cnt))

    while q:
        nowY, nowX, cnt = q.popleft()
        if nowY == n-1 and nowX == m-1:
            return cnt+1
        for i in range(4):
            dy = nowY + directY[i]
            dx = nowX + directX[i]
            if 0 <= dy < n and 0 <= dx < m:
                if used[dy][dx] == 0 and lst[dy][dx] == 1:
                    used[dy][dx] = 1
                    q.append((dy, dx, cnt+1))

used = [[0]*m for _ in range(n)]
res = bfs(0,0,0)
print(res)