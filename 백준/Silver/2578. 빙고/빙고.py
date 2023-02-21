def bing():
    total = 0

    # 가로 방향 체크
    for i in range(5):
        cnt = 0
        for j in range(5):
            if lst[i][j] == 'X':
                cnt += 1
        if cnt == 5:
            total += 1

    # 세로 방향 체크
    for i in range(5):
        cnt = 0
        for j in range(5):
            if lst[j][i] == 'X':
                cnt += 1
        if cnt == 5:
            total += 1

    # 오른쪽 대각선 방향 체크
    cnt = 0
    for i in range(5):
        if lst[i][i] == 'X':
            cnt += 1
    if cnt == 5:
        total += 1

    # 왼쪽 대각선 방향 체크
    cnt = 0
    for i in range(5):
        if lst[i][-i-1] == 'X':
            cnt += 1
    if cnt == 5:
        total += 1

    if total >= 3:
        return True
    else:
        return False



lst = []
call = []

for i in range(5):
    lst.append(list(map(int, input().split())))

for i in range(5):
    call.append(list(map(int, input().split())))

    
   
n = 0
flag = 0
for i in range(5):
    for j in range(5):
        findv = call[i][j]
        for k in range(5):
            for g in range(5):
                if lst[k][g] == findv:
                    n += 1
                    lst[k][g] = 'X'
                    if bing():
                        print(n)
                        flag = 1
                        break
        if flag:
            break
    if flag:
        break

