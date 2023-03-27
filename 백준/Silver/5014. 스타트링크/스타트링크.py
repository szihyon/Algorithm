from collections import deque

f, s, g, u, d = map(int, input().split())

def bfs(st, cnt):
    q = deque()
    q.append((st,cnt))

    while q:
        now, cnt = q.popleft()
        if now == g-1:
            return cnt
        for i in [u, -d]:
            if now+i < 0 or now+i > f-1: continue
            if used[now+i] == 1: continue
            used[now + i] = 1
            q.append((now+i, cnt+1))

    return "use the stairs"

used = [0]*f
res = bfs(s-1, 0)
print(res)