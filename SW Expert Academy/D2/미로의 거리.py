# BFS
from  collections import deque

T = int(input())

def check(y, x, cnt):
    q = deque()
    q.append((y, x, cnt))

    while q:
        y, x, cnt = q.popleft()
        if y == edY and x == edX:
            return cnt-1

        for i in range(4):
            dy = y + directionY[i]
            dx = x + directionX[i]
            if dy < 0 or dx < 0 or dy > n-1 or dx > n-1: continue
            if lst[dy][dx] == 1: continue
            if visit[dy][dx] == 1: continue
            visit[dy][dx] = 1
            q.append((dy, dx, cnt+1))

    return 0

for tc in range(1, T+1):
    n = int(input())
    lst = []
    for i in range(n):
        lst.append(list(map(int, input())))
    for i in range(n):
        for j in range(n):
            if lst[i][j] == 2:
                stY = i
                stX = j
            if lst[i][j] == 3:
                edY = i
                edX = j
    directionY = [-1, 0, 0, 1]
    directionX = [0, -1, 1, 0]
    visit = [[0]*n for _ in range(n)]
    visit[stY][stX] = 1
    res = check(stY, stX, 0)
    if res:
        print(f"#{tc} {res}")
    else:
        print(f"#{tc} {0}")

        
###############################################
# DFS
T = int(input())

def check(y, x, Sum):
    global Min
    if y == edY and x == edX:
        if Sum < Min:
            Min = Sum
        return

    for i in range(4):
        dy = directionY[i] + y
        dx = directionX[i] + x
        if dy < 0 or dx < 0 or dy > n - 1 or dx > n - 1: continue
        if visit[dy][dx] == 1: continue
        if lst[dy][dx] == 1: continue
        visit[dy][dx] = 1
        check(dy, dx, Sum + 1)
        visit[dy][dx] = 0


for tc in range(1, T+1):
    n = int(input())
    lst = []
    for i in range(n):
        lst.append(list(map(int, input())))
    for i in range(n):
        for j in range(n):
            if lst[i][j] == 2:
                stY = i
                stX = j
            if lst[i][j] == 3:
                edY = i
                edX = j
    directionY = [-1, 0, 0, 1]
    directionX = [0, -1, 1, 0]
    visit = [[0]*n for _ in range(n)]
    visit[stY][stX] = 1
    Min = 21e8
    check(stY, stX, 0)
    if Min == 21e8:
        print(f"#{tc} {0}")
    else:
        print(f"#{tc} {Min-1}")
