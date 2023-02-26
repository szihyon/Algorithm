T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    pizza = list(map(int, input().split()))
    cook = []

    for i in range(1, N+1):
        cook.append([i, pizza.pop(0)])

    while cook:
        check = cook.pop(0)
        check[1] //= 2
        if check[1] != 0:
            cook.append(check)
        else:
            if pizza:
                i += 1
                cook.append([i, pizza.pop(0)])
    print(f"#{tc} {check[0]}")
