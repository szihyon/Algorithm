n = int(input())
student = [i+1 for i in range(n)]
lst = list(map(int, input().split()))
lst2 = []
for i in range(n):
    if lst[i] == 0:
        lst2.append(student[i])
    else:
        lst2.insert(-lst[i], student[i])
print(*lst2)
