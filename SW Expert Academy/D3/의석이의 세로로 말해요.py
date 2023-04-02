T = int(input())
for tc in range(1, T+1):
    lst = [['#']*15 for _ in range(5)]
    for i in range(5):
        word = input()
        n = len(word)
        for j in range(n):
            lst[i][j] = word[j]
    print(f"#{tc}", end=' ')
    for i in range(15):
        for j in range(5):
            if lst[j][i] != "#":
                print(lst[j][i], end='')
    print()
