n = int(input())

for i in range(n):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a_card = sorted(a[1:])
    b_card = sorted(b[1:])
    card = [5, 4, 3, 2, 1]
    flag = 0
    for i in range(len(card)):
        if a_card.count(card[i]) > b_card.count(card[i]):
            print("A")
            flag = 1
            break
        elif a_card.count(card[i]) < b_card.count(card[i]):
            print("B")
            flag = 1
            break
    if flag == 0:
        print("D")