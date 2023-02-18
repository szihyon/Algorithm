def dfs(now):
    ans.append(lst1[now])
    for i in range(len(lst2)):
        if lst2[now][i] == 1 and used[i] == 0:
            used[i] = 1
            dfs(i)
            used[i] = 0

T = int(input())
for tc in range(1, T+1):
    v, e = map(int, input().split())
    lst1 = [i+1 for i in range(v)]
    lst2 = [[0]*v for _ in range(v)]
    used = [0]*len(lst1)
    ans = []
    for i in range(e):
        st, ed = map(int, input().split())
        lst2[st-1][ed-1] = 1
    s, g = map(int, input().split())
    dfs(s-1)
    if g in ans:
        print(f"#{tc} 1")
    else:
        print(f"#{tc} 0")
