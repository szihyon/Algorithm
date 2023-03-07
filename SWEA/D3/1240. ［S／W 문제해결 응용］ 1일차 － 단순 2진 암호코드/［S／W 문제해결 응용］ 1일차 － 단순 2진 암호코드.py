codes = [[0,0,0,1,1,0,1],[0,0,1,1,0,0,1],[0,0,1,0,0,1,1],[0,1,1,1,1,0,1],[0,1,0,0,0,1,1],[0,1,1,0,0,0,1],[0,1,0,1,1,1,1],[0,1,1,1,0,1,1],[0,1,1,0,1,1,1],[0,0,0,1,0,1,1]]

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())    # 세로n 가로m
    lst = []
    for i in range(n):
        lst.append(list(map(int, input())))
    for i in range(n):
        cnt = 0
        for j in range(m):
            if lst[i][j] == 0:
                cnt += 1
        if cnt != m:
            idx = i
            break
    code = lst[idx]
    # print(code)
    last_idx = 0
    check = []
    for i in range(m-1, 0, -1):
        if code[i] == 1:
            last_idx = i
            break

    for i in range(last_idx, 0, -7):
        if code[i-6:i+1] in codes:
            check.append(code[i-6:i+1])
        else:
            break

    check2 = []
    for i in range(len(check)):
        check2.append(codes.index(check[i]))
    check2 = check2[::-1]

    odd = check2[0:len(check2):2]
    even = check2[1:len(check2):2]
    check_num = sum(odd)*3 + sum(even)
    if check_num % 10 == 0:
        ans = sum(odd) + sum(even)
    else:
        ans = 0

    print(f"#{tc} {ans}")