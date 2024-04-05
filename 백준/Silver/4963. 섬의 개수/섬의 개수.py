from collections import deque

def bfs(stY, stX):
    dirY = [-1, -1, -1, 0, 0, 1, 1, 1]
    dirX = [-1, 0, 1, -1, 1, -1, 0, 1]
    q = deque()
    q.append([stY, stX])
    while q:
        nowY, nowX = q.popleft()
        for i in range(8):
            dy = dirY[i] + nowY
            dx = dirX[i] + nowX
            if dy < 0 or dx < 0 or dy > h-1 or dx > w-1: continue
            if square_map[dy][dx] == 1:
                square_map[dy][dx] = 0
                q.append([dy, dx])

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0: break
    square_map = []
    for _ in range(h):
        square_map.append(list(map(int, input().split())))
    cnt = 0
    for i in range(h):
        for j in range(w):
            if square_map[i][j] == 1:
                cnt += 1
                bfs(i, j)
    print(cnt)