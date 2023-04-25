# https://www.acmicpc.net/problem/11724

n, m = map(int, input().split())
lst = [[0]*n for _ in range(n)]
for _ in range(m):
    p1, p2 = map(int, input().split())
    lst[p1-1][p2-1] = 1
    lst[p2-1][p1-1] = 1
