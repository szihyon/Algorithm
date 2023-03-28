from collections import deque
import copy

n = int(input())
lst = []

for i in range(n):
    lst.append(list(map(int, input().split())))

lst2 = copy.deepcopy(lst)

maX = 0
for i in range(len(lst)):
    for j in range(len(lst[i])):
        if lst[i][j] > maX:
            maX = lst[i][j]


def bfs(y, x):
    q = deque()
    q.append((y, x))

    directY = [-1, 0, 0, 1]
    directX = [0, -1, 1, 0]

    while q:
        y, x = q.popleft()

        for i in range(4):
            dy = directY[i] + y
            dx = directX[i] + x
            if dy < 0 or dx < 0 or dy > n-1 or dx > n-1: continue
            if lst2[dy][dx] == 1:
                lst2[dy][dx] = 0 
                q.append((dy, dx))

    return 


max_cnt = 0
for k in range(maX):

    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] <= k:
                lst2[i][j] = 0
            else:
                lst2[i][j] = 1

    cnt = 0
    for i in range(len(lst2)):
        for j in range(len(lst2[i])):
            if lst2[i][j] == 1:
                bfs(i, j)
                cnt += 1

    if cnt > max_cnt:
        max_cnt = cnt


print(max_cnt)