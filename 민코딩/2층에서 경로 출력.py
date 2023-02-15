lst = []
n = int(input())
for i in range(n):
    lst.append(list(map(int, input().split())))
path = [0]*3

def abc(now, level):
    global path
    path[level] = now
    if level == 2:
        print(*path)
        return

    for i in range(n):
        if lst[now][i] == 1:
            abc(i, level+1)

abc(0,0)
