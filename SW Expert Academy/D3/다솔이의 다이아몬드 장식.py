T = int(input())
 
for tc in range(1, T+1):
    st = list(input())
    n = len(st)*4 + 1
    lst = [['.']*n for _ in range(5)]
 
    # 첫번째 줄, 다섯번째 줄
    for j in range(len(lst)):
        for i in range(n):
            if 4*j < len(lst) and 4*i+2 <n:
                lst[4*j][4*i+2] = '#'
 
    # 두번째 줄, 네번째 줄
    for j in range(len(lst)):
        for i in range(n):
            if 2*j+1 < len(lst) and 2*i+1 <n:
                lst[2*j+1][2*i+1] = '#'
 
 
    # 세번째 줄
    for i in range(n):
        if 4*i < n:
            lst[2][4*i] = '#'
 
    for i in range(n):
        if 4*i+2 < n:
            lst[2][4*i+2] = st[i]
 
 
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            print(lst[i][j], end='')
        print()
