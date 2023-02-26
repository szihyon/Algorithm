# BFS
from collections import deque

def bfs(y, x):
    q = deque()
    q.append((y,x))

    while q:
        y, x = q.popleft()
        for i in range(4):
            dy = directY[i] + y
            dx = directX[i] + x
            if dy < 0 or dx < 0 or dy > 15 or dx > 15: continue
            if lst[dy][dx] == 3: return True
            if lst[dy][dx] == 1: continue
            if visit[dy][dx] == 1: continue
            visit[dy][dx] = 1
            q.append((dy, dx))
    return False

for _ in range(10):
    tc = int(input())
    lst = []
    for i in range(16):
        lst.append(list(map(int, input())))
    for i in range(16):
        for j in range(16):
            if lst[i][j] == 2:
                stY = i
                stX = j
                break
    directY = [1, -1, 0, 0]
    directX = [0, 0, -1, 1]
    visit = [[0]*16 for _ in range(16)]
    visit[stY][stX] = 1
    if bfs(stY, stX):
        print(f"#{tc} {1}")
    else:
        print(f"#{tc} {0}")
