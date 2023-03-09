
for tc in range(1, 11):
    length = int(input())
    lst = []
    for _ in range(length):
        lst.append(list(map(int, input().split())))
    cnt = 0
    for i in range(length):
        check = []
        for j in range(length):
            if lst[j][i] == 1:
                check.append(1)
            elif lst[j][i] == 2:
                check.append(2)
        for i in range(len(check) - 1):
            if check[i] == 1:
                if check[i + 1] == 2:
                    cnt += 1

    print(f"#{tc} {cnt}")