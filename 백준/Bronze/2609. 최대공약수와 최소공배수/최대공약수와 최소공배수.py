A, B = map(int, input().split())
maxV = max(A, B)

ans1 = 0
for i in range(1, maxV+1):
    if A % i == 0 and B % i == 0:
        ans1 = i

ans2 = ans1 * (A // ans1) * (B // ans1)

print(ans1)
print(ans2)