import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


N, M, R = map(int, input().split())

# lst = [[0]*N for _ in range(N)] 메모리초과
lst = [[] for _ in range(N)]

for _ in range(M):
    S, E = map(int, input().split())
    # lst[S-1][E-1] = 1
    # lst[E-1][S-1] = 1
    lst[S-1].append(E-1)
    lst[E-1].append(S-1)

for i in range(N):
    lst[i].sort() #오름차순 방문

visited = [-1]*N

def dfs(now, level):
    # for i in range(N):
        # if lst[now][i] == 1 and visited[i] == -1:
    for next in lst[now]:
        if visited[next] == -1:
            visited[next] = level 
            dfs(next, level+1)

visited[R-1] = 0
dfs(R-1, 1)

for i in range(N):
    print(visited[i])