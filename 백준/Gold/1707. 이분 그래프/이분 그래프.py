from collections import deque

def bfs(start):
    q = deque()
    q.append(start)
    used[start] = 1
    while q:
        now = q.popleft()
        for i in lst[now]:
            if used[i] == 0:
                used[i] = -used[now]
                q.append(i)
            else:
                if used[now] == used[i]:
                    return False
    return True


K = int(input())
for _ in range(K):
    V, E = map(int, input().split())
    lst = [[] for _ in range(V+1)]
    used = [0]*(V+1)
    for i in range(E):
        u, v = map(int, input().split())
        lst[u].append(v)
        lst[v].append(u)
    for i in range(1, V+1):
        if used[i] == 0:
            res = bfs(i)
            if not res:
                break
    if res:
        print("YES")
    else:
        print("NO")