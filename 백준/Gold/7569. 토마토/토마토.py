from collections import deque

m, n, h = map(int, input().split())
lst1 = []
lst2 = []

for i in range(h):
    lst2 = []
    for j in range(n):
        lst2.append(list(map(int, input().split())))
    lst1.append(lst2)

##############################################

def bfs(h, n, m, lst1):
    q = deque()

    cnt = 0
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if lst1[i][j][k] == 1:
                    q.append((i, j, k, 0))
                elif lst1[i][j][k] == 0:
                    cnt += 1

    if cnt == 0:
        return 0

    # 상하좌우앞뒤
    directH = [-1, 1, 0, 0, 0, 0]
    directN = [0, 0, -1, 1, 0, 0]
    directM = [0, 0, 0, 0, -1, 1]

    while q:
        h2, n2, m2, day = q.popleft()

        for i in range(6):
            dh = h2 + directH[i]
            dn = n2 + directN[i]
            dm = m2 + directM[i]
            if dm < 0 or dm > m-1 or dn < 0 or dn > n-1 or dh < 0 or dh > h-1:continue
            if lst1[dh][dn][dm] == -1: continue
            if lst1[dh][dn][dm] == 0:
                lst1[dh][dn][dm] = 1
                q.append((dh, dn, dm, day+1))

    def check(h, n, m, lst1):
        for i in range(h):
            for j in range(n):
                for k in range(m):
                    if lst1[i][j][k] == 0:
                        return False
        return True

    if check(h, n, m, lst1):
        return day
    else:
        return -1

print(bfs(h, n, m, lst1))