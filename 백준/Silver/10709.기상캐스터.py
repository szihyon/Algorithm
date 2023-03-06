h, w = map(int, input().split())        # h는 y, w는 x / 1분 후 동쪽 이동
lst = []
for _ in range(h):
    lst.append(list(input()))
for i in range(h):
    flag = 0
    time = 0
    for j in range(w):
        if lst[i][j] == 'c':
            lst[i][j] = 0
            flag = 1
            time = 1
        elif lst[i][j] == '.':
            if flag == 0:
                lst[i][j] = -1
            else:
                lst[i][j] = time-1
        if time:
            time += 1

for i in range(len(lst)):
    for j in range(len(lst[i])):
        print(lst[i][j], end=' ')
    print()
