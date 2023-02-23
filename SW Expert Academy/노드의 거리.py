# 풀이 1
# DFS

T = int(input())


def dfs(S, cnt, G):
    global min

    if cnt > min: return

    if S == G:
        if cnt < min:
            min = cnt
        return min

    for i in range(len(lst)):
        if lst[S][i] == 1 and used[i] == 0:
            used[i] = 1
            dfs(i, cnt + 1, G)
            used[i] = 0


for tc in range(1, T + 1):
    V, E = map(int, input().split())
    lst = [[0] * V for _ in range(V)]
    for i in range(E):
        r1, r2 = map(int, input().split())
        r1 = r1 - 1
        r2 = r2 - 1
        lst[r1][r2] = 1
        lst[r2][r1] = 1
    S, G = map(int, input().split())
    S = S - 1
    G = G - 1
    used = [0] * V
    min = 21e8
    used[S] = 1
    res = dfs(S, 0, G)

    if min == 21e8:
        print(f"#{tc} 0")
    else:
        print(f"#{tc} {min}")



#######################################################################

# 풀이2
# BFS

T = int(input())


def bfs(start, end):
    queue = [(start, 0)]
    visited = []
    while queue:
        node, cnt = queue.pop(0)
        if node == end:
            return cnt
        if node not in visited:
            visited.append(node)
            for i in range(V):
                if i not in visited and arr[node][i] == 1:
                    queue.append((i, cnt + 1))
    else:
        return 0


for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    arr = [[0] * V for _ in range(V)]
    for _ in range(E):
        st, ed = map(int, input().split())
        st -= 1
        ed -= 1
        arr[st][ed], arr[ed][st] = 1, 1

    start, end = map(int, input().split())
    start -= 1
    end -= 1
    result = bfs(start, end)
    print(f'#{test_case} {result}')
