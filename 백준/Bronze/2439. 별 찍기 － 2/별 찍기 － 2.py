n = int(input())
lst = []

for i in range(1, n+1):
    content = " " * (n-i) + "*" * (i)
    lst.append(content)

for i in range(n):
    print(lst[i])