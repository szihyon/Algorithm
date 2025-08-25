from collections import deque

n, m = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

flag = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            targetY = i
            targetX = j 
            flag = 1
            break
    if flag: break

distance = [[-1]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            distance[i][j] = 0

queue = deque([(targetY, targetX, 0)])
distance[targetY][targetX] = 0

directY = [-1, 1, 0, 0]
directX = [0, 0, -1, 1]

while queue:
    nowY, nowX, dist = queue.popleft()
    for i in range(4):
        nextY = nowY + directY[i]
        nextX = nowX + directX[i]
        if nextY<0 or nextX<0 or nextY>n-1 or nextX>m-1:continue
        if graph[nextY][nextX] == 1 and distance[nextY][nextX] == -1:
            distance[nextY][nextX] = dist + 1
            queue.append((nextY, nextX, dist + 1))
 
for i in range(n):
    print(' '.join(map(str, distance[i])))
