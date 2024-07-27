T = int(input())
buttons = [300, 60, 10]
answer = []

for i in range(3):
    answer.append(T // buttons[i])
    T = T % buttons[i]

if T == 0:
    print(*answer)
else:
    print(-1)