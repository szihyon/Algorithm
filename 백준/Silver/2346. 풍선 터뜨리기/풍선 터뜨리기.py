n = int(input())
lst = list(map(int, input().split()))
lst = [[num+1, val] for num, val in enumerate(lst)]
answer = []

idx = 0

for _ in range(n):
    temp = lst.pop(idx)
    answer.append(temp[0])
    if temp[1] > 0 and lst:
        idx = (idx + temp[1] - 1) % len(lst)
    elif temp[1] < 0 and lst:
        idx = (idx + temp[1]) % len(lst)

print(*answer)