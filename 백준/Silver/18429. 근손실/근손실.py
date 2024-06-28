N, K = map(int, input().split())
kits = list(map(int, input().split()))
used = [0]*N
answer = []

def dfs(day, nowK, comb):
    global answer
    if day > 0:
        nowK -= K
        nowK += kits[comb[-1]]
        if nowK < 500:
            return

    if day == N:
        answer.append(comb)
        return

    for i in range(N):
        if used[i] == 1: continue
        used[i] = 1
        dfs(day+1, nowK, comb+[i])
        used[i] = 0

dfs(0, 500, [])
print(len(answer))