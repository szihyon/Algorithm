e, s, m = map(int, input().split())

E = S = M = 0
year = 0
while True:
    year += 1
    E += 1
    S += 1
    M += 1
    if E == 16:
        E = 1
    if S == 29:
        S = 1
    if M == 20:
        M = 1

    if E==e and S==s and M==m:
        break

print(year)