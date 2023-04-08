import copy
from collections import deque

n, m = map(int, input().split())
lst = []

for i in range(n):
    lst.append(list(map(int, input().split())))


def bfs(stY, stX, lst2):
    directY = [-1, 0, 0, 1]
    directX = [0, -1, 1, 0]
    q = deque()
    q.append((stY, stX))
    while q:
        nowY, nowX = q.popleft()
        for i in range(4):
            dy = directY[i] + nowY
            dx = directX[i] + nowX
            if dy < 0 or dx < 0 or dy > n-1 or dx > m-1: continue
            if lst2[dy][dx] == 2: continue
            if lst2[dy][dx] == 1: continue
            lst2[dy][dx] = 1
            q.append((dy, dx))


def dfs(level, start):
    global M_cnt
    if level == 3:
        lst2 = copy.deepcopy(lst)
        cnt = 0
        for i in range(3):
            y, x = path[i]
            lst2[y][x] = 1
        for i in range(len(lst2)):
            for j in range(len(lst2[i])):
                if lst2[i][j] == 2:
                    bfs(i, j, lst2)
        for i in range(len(lst2)):
            for j in range(len(lst2[i])):
                if lst2[i][j] == 0:
                    cnt += 1
        if cnt > M_cnt:
            M_cnt = cnt
        return
    for i in range(start, n*m):
        row, col = divmod(i, m)
        if lst[row][col] != 0: continue
        path[level] = [row, col]
        dfs(level+1, i+1)


path = [0]*3
M_cnt = 0
dfs(0, 0)
print(M_cnt)