from collections import deque
n = int(input())
lst = [[0]*n for _ in range(n)]
p1, p2 = map(int, input().split())
m = int(input())
for i in range(m):
    a, b = map(int, input().split())
    lst[a-1][b-1] = 1
    lst[b-1][a-1] = 1

def bfs(p1, cnt):
    q = deque()
    q.append((p1,cnt))
    used = [0]*n

    while q:
        now, cnt = q.popleft()
        if now == p2-1:
            return cnt
        for i in range(n):
            if used[i] == 0:
                if lst[now][i] == 1:
                    used[i] = 1
                    q.append((i, cnt+1))
    return -1

res = bfs(p1-1, 0)
print(res)