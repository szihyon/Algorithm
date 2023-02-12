import sys
sys.stdin = open("input.txt", "r")

T = int(input())

def sum_t(i, j, lst, m):
    direct_y = [-1, 0, 0, 1]
    direct_x = [0, -1, 1, 0]
    sumv1 = lst[i][j]
    for k in range(4):
        for g in range(1, m):
            dy = i + direct_y[k] * g
            dx = j + direct_x[k] * g
            if dy < 0 or dx < 0 or dy > len(lst)-1 or dx > len(lst)-1:
                continue
            sumv1 += lst[dy][dx]
    return sumv1

def sum_x(i, j, lst, m):
    direct_y = [-1, -1, 1, 1]
    direct_x = [-1, 1, -1, 1]
    sumv2 = lst[i][j]
    for k in range(4):
        for g in range(1, m):
            dy = i + direct_y[k] * g
            dx = j + direct_x[k] * g
            if dy < 0 or dx < 0 or dy > len(lst)-1 or dx > len(lst)-1:
                continue
            sumv2 += lst[dy][dx]
    return sumv2

for tc in range(1, T+1):
    n, m = map(int, input().split())
    lst = []
    for i in range(n):
        lst.append(list(map(int, input().split())))
    maxv = 0
    for i in range(n):
        for j in range(n):
            res1 = sum_x(i, j, lst, m)
            res2 = sum_t(i, j, lst, m)
            if res1 > res2:
                res = res1
            else:
                res = res2
            if res > maxv:
                maxv = res
    print(f"#{tc} {maxv}")