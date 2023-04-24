from collections import deque
import copy
n = int(input())
lst1 = [list(input()) for _ in range(n)]
lst2 = copy.deepcopy(lst1)

for i in range(n):
    for j in range(n):
        if lst2[i][j] == 'R':
            lst2[i][j] = "G"

def bfs(stY, stX, st, lst):
    directY = [-1, 0, 0, 1]
    directX = [0, -1, 1, 0]
    q = deque()
    q.append((stY, stX))
    used = [[0]*n for _ in range(n)]
    used[stY][stX] = 1

    while q:
        nowY, nowX = q.popleft()
        for i in range(4):
            dy = directY[i] + nowY
            dx = directX[i] + nowX
            if dy < 0 or dx < 0 or dy > n-1 or dx > n-1:continue
            if used[dy][dx] == 1: continue
            if lst[dy][dx] == st:
                used[dy][dx] = 1
                lst[dy][dx] = 0
                q.append((dy, dx))

cnt = 0
for i in range(n):
    for j in range(n):
        if lst1[i][j] != 0:
            cnt += 1
            bfs(i, j, lst1[i][j], lst1)

cnt2 = 0
for i in range(n):
    for j in range(n):
        if lst2[i][j] != 0:
            cnt2 += 1
            bfs(i, j, lst2[i][j], lst2)

print(f"{cnt} {cnt2}")