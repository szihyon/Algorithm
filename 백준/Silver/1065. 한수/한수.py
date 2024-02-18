n = int(input())

answer = 0
for number in range(1, n+1):
    if number < 100:
        answer += 1
    if number >= 100:
        number = list(str(number))
        diff = []
        for i in range(len(number)-1):
            diff.append(int(number[i+1]) - int(number[i]))
        if diff.count(diff[0]) == len(diff):
            answer += 1

print(answer)