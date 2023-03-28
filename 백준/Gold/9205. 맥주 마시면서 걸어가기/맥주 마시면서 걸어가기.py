from collections import deque

T = int(input())


def bfs(stX, stY):
    q = deque()
    q.append((stX, stY))

    while q:
        nowx, nowy = q.popleft()
        if abs(edX - nowx) + abs(edY - nowy) <= 1000:
            return "happy"

        for i in range(conv):
            if used[i] == 0:
                if abs(conv_lst[i][0] - nowx) + abs(conv_lst[i][1] - nowy) <= 1000:
                    used[i] = 1
                    q.append((conv_lst[i][0], conv_lst[i][1]))

    return 'sad'


for tc in range(T):
    conv = int(input())
    stX, stY = map(int, input().split())
    conv_lst = []
    for i in range(conv):
        x, y = map(int, input().split())
        conv_lst.append((x, y))
    edX, edY = map(int, input().split())

    used = [0] * conv
    res = bfs(stX, stY)
    print(res)
