T = int(input())

def abc(level):
    global minV
    if level == n:
        sumV = 0
        for k in range(len(path)-1):
            sumV += lst[path[k]][path[k+1]]
        if sumV < minV:
            minV = sumV
        return

    for i in range(len(route)):
        if used[i] == 1:continue
        used[i] = 1
        path[level] = route[i]
        abc(level+1)
        used[i] = 0


for tc in range(1, T+1):
    n = int(input())
    lst = []
    for i in range(n):
        lst.append(list(map(int, input().split())))
    route = [(i+1) for i in range(n-1)]
    path = [0] * (n+1)
    path[0] = path[-1] = 0
    used = [0]*len(route)
    minV = 21e8
    abc(1)
    print(f"#{tc} {minV}")
