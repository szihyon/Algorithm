from collections import deque

N, M = map(int, input().split())

arr = [[] for _ in range(N+1)]
for i in range(M):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

def bfs(start):
    visited = [-1] * (N + 1)
    q = deque()
    q.append(start)
    visited[start] = 0

    while q:
        node = q.popleft()
        for next_node in arr[node]:
            if visited[next_node] == -1:
                visited[next_node] = visited[node] + 1
                q.append(next_node)
    total = sum(visited)
    return total

min_total = float("INF")
ans = 0
for i in range(1, N+1):
    total = bfs(i)
    if total < min_total:
        min_total = total
        ans = i

print(ans)