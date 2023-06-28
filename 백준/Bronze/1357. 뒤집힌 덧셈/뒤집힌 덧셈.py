x, y = input().split()
ans = str(int(x[::-1]) + int(y[::-1]))[::-1]
for i in range(len(ans)):
    if ans[i] != "0":
        break
print(ans[i:])