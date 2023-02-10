T = int(input())

def check(y, x):
    Sum = 0
    directionY = [-1, 0, 0, 0, 1]
    directionX = [0, -1, 0, 1, 0]
    for i in range(5):
        dy = directionY[i] + y
        dx = directionX[i] + x
        if dy < 0 or dx < 0 or dy > n-1 or dx > m-1:
            continue
        Sum += lst[dy][dx]
    return Sum

for tc in range(1, T+1):
    n, m = map(int, input().split())
    lst = [list(map(int, input().split())) for i in range(n)]
    Max = 0
    for i in range(n):
        for j in range(m):
            res = check(i, j)
            if res > Max:
                Max = res
    print(f"#{tc} {Max}")
