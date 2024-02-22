T = int(input())
for i in range(T):
    A, B = map(int, input().split())
    maxV = max(A, B)
    for i in range(1, maxV+1):
        if A % i == 0 and B % i == 0:
            gcd = i
    print(gcd * (A // gcd) * (B // gcd))
