from collections import deque

n, m, v = map(int, input().split())
lst = [[0]*n for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    lst[a-1][b-1] = 1
    lst[b-1][a-1] = 1

def dfs(now, level):
    print(now+1, end=' ')

    for i in range(n):
        if visit[i] == 1:continue
        if lst[now][i] == 1:
            visit[i] = 1
            dfs(i, level+1)

visit = [0]*n
visit[v-1] = 1
dfs(v-1, 0)
print()



def bfs(st):
    q = deque()
    q.append(st)

    while q:
        now = q.popleft()
        print(now+1, end=" ")

        for i in range(len(lst)):
            if lst[now][i] == 1 and used[i] == 0:
                used[i] = 1
                q.append((i))

used = [0]*len(lst)
used[v-1] = 1
bfs(v-1)