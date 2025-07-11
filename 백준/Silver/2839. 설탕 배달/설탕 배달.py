N = int(input())

answer = -1
for i in range(N // 5, -1, -1):  # 5kg 봉지를 최대한 많이 쓰는 쪽부터
    remain = N - (i * 5)
    if remain % 3 == 0:
        answer = i + (remain // 3)
        break

print(answer)