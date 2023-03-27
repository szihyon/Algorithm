n, k = map(int, input().split())

def bfs(st, time):
    q = []
    q.append((st, time))

    while q:
        now, time = q.pop(0)
        if now == k:
            return time
        for i in [-1, 1, now]:
            if now + i < 0 or now + i > 200000: continue
            if used[now + i] == 1: continue
            used[now + i] = 1
            q.append((now+i, time+1))
    return -1

used = [0]*200001
used[n] = 1
res = bfs(n, 0)
print(res)