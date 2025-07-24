N, M = map(int, input().split())
lst = []
for _ in range(M):
    lst.append(list(map(int, input().split())))
visited = [[0]*N for _ in range(M)]

flag = 0
def dfs(y, x):
    global flag
    dy = [0, 1] #동쪽, 남쪽
    dx = [1, 0]

    if y == M-1 and x == N-1:
        flag = 1
        return
    
    for i in range(2):
        if y+dy[i]<0 or y+dy[i]>M-1: continue
        if x+dx[i]<0 or x+dx[i]>N-1: continue
        if visited[y+dy[i]][x+dx[i]] == 1: continue
        if lst[y+dy[i]][x+dx[i]] == 0: continue
        visited[y+dy[i]][x+dx[i]] = 1
        dfs(y+dy[i], x+dx[i])

if lst[0][0] == 1:
    visited[0][0] = 1
    dfs(0, 0)

if flag:
    print("Yes")
else:
    print("No")