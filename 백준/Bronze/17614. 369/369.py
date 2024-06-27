N = int(input())
clap = [3, 6, 9]
total = 0

for num in range(1, N+1):
    num = list(map(int, list(str(num))))
    for i in range(len(num)):
        if num[i] in clap:
            total += 1

print(total)