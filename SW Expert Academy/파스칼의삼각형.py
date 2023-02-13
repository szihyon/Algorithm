T = int(input())

for tc in range(1, T+1):
    n = int(input())
    lst = [[0 for _ in range(n+1)] for _ in range(n+1)]
    lst[1][1] = 1
    for i in range(2, n+1):
        for j in range(1, i+1):
            lst[i][j] = lst[i-1][j] + lst[i-1][j-1]

    print(f"#{tc}")
    for i in range(1, 1+n):
        for j in range(1, i+1):
            print(lst[i][j], end=" ")
        print()

