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

    
# 방법 2
# T = int(input())
# for tc in range(1, T+1):
#     arr = [input() for _ in range(5)]
#     ans = ''
#     for j in range(15):
#         for i in range(5):
#             if j < len(arr[i]):
#                 ans += arr[i][j]
#     print(f"#{tc} {ans}")
