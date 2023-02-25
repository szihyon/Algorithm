def game(i, j):
    if lst[i] == 1:
        if lst[j] == 2:
            return j
        elif lst[j] == 3:
            return i
        else:
            return i
    elif lst[i] == 2:
        if lst[j] == 3:
            return j
        elif lst[j] == 1:
            return i
        else:
            return i
    elif lst[i] == 3:
        if lst[j] == 1:
            return j
        elif lst[j] == 2:
            return i
        else:
            return i


def winner(i,j):
    # print("winner",i,j)
    if j-i == 1:
        return game(i, j)
    elif i == j:
        return i
    a = winner(i, (i+j) // 2)
    b = winner((i+j) // 2 + 1, j)
    return game(a, b)

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    lst = list(map(int, input().split()))
    # print(lst)
    print(f"#{tc} {winner(0, n-1)+1}")
