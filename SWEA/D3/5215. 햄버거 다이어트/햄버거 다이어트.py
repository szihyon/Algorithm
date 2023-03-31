T = int(input())

def abc(level, start, score, kal):
    global max_score

    if score > max_score:
        max_score = score

    if level == n:
        return

    for i in range(start, n):
        if kal+lst[i][1] <= l:
            abc(level+1, i+1, score+lst[i][0], kal+lst[i][1])


for tc in range(1, T+1):
    n, l = map(int, input().split())
    lst = []
    for i in range(n):
        # 점수, 칼로리
        t, k = map(int, input().split())
        lst.append([t, k])
    max_score = 0
    abc(0, 0, 0, 0)
    print(f"#{tc} {max_score}")