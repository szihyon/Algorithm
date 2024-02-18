from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
computers = [[] for i in range(n)]

for i in range(m):
    c1, c2 = map(int, input().split())
    computers[c2-1].append(c1)

def bfs(start):
    q = deque()
    q.append(start)
    cnt = 0

    used = [0] * n
    used[start] = 1

    while q:
        now = q.popleft()
        cnt += 1
        for i in computers[now]:
            if used[i-1] == 0:
                used[i-1] = 1
                q.append(i-1)
    return cnt

result = []
for i in range(n):
    result.append(bfs(i))

for i in range(n):
    if result[i] == max(result):
        print(i+1, end=' ')