n = int(input())

for i in range(n):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a_card = a[1:] # a카드목록
    b_card = b[1:] # b카드목록
    card = [5, 4, 3, 2, 1] # 카드 배점 큰 순서로 나열
    flag = 0
    for i in range(len(card)): # 배점 큰 카드부터 비교
        if a_card.count(card[i]) > b_card.count(card[i]): # 카드 각자 몇 개 있는지 체크
            print("A")  # a가 더 많으면 A출력 후 break
            flag = 1
            break
        elif a_card.count(card[i]) < b_card.count(card[i]):
            print("B") # b가 더 많으면 B출력 후 break
            flag = 1
            break
    if flag == 0: # flag가 안켜졌다면 무승부
        print("D")