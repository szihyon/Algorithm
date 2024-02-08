import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n, m, r = map(int, input().split())
lst = [[] for _ in range(n+1)]
res = [0]*(n+1)

for i in range(m):
    n1, n2 = map(int, input().split())
    lst[n1].append(n2)
    lst[n2].append(n1)

for i in range(1, len(lst)):
    lst[i].sort(reverse=True)

cnt = 1
def dfs(node):
    global cnt
    res[node] = cnt

    for n in lst[node]:
        if res[n]: continue
        cnt += 1
        dfs(n)

res[r] = 1
dfs(r)

for i in res[1:]:
    print(i)