from collections import deque

c = int(input())
n = int(input())
lst = [[0]*c for _ in range(c)]

for i in range(n):
    a, b = map(int, input().split())
    lst[a-1][b-1] = 1
    lst[b-1][a-1] = 1

def bfs(st):
    cnt = 0
    q = deque()
    q.append(st)

    while q:
        now = q.popleft()
        cnt += 1
        for i in range(c):
            if used[i] == 0 and lst[now][i] == 1:
                used[i] = 1
                q.append(i) 

    return cnt-1

used = [0]*c
used[0] = 1
res = bfs(0)
print(res)