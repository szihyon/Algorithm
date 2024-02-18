from collections import deque

N, M, R = map(int, input().split())
lst = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    lst[u].append(v)
    lst[v].append(u)

for i in range(N+1):
    lst[i].sort()

def bfs(start):
    global visit
    q = deque()
    q.append(start)
    visit = [0]*(N+1)
    cnt = 1
    visit[start] = cnt

    while q:
        now = q.popleft()
        for node in lst[now]:
            if visit[node] >= 1: continue
            cnt += 1
            visit[node] = cnt
            q.append(node)
    return

bfs(R)
for i in range(1, len(visit)):
    print(visit[i])
