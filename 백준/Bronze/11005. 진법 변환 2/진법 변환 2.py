N, B = map(int, input().split())
lst = []
while N >= B:
    r = N % B
    N = N // B
    lst.append(r)
lst.append(N)
lst.reverse()
for i in range(len(lst)):
    if lst[i] >= 10:
        lst[i] = chr(lst[i]+55)
    else:
        lst[i] = str(lst[i])

answer = ''.join(lst)
print(answer)