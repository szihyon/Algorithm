T = int(input())
lst = list(map(int, input().split()))
lst.sort()
sum = 0
for i in range(T):
    for j in range(0, i+1):
        sum += lst[j]
print(sum)