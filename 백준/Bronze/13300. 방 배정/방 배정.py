n, k = map(int, input().split())

man = {}
woman = {}

for i in range(n):
    s, year = map(int, input().split())
    if s == 0:
        if year in woman:
            woman[year] += 1
        else:
            woman[year] = 1
    else:
        if year in man:
            man[year] += 1
        else:
            man[year] = 1

rooms = 0
woman = list(woman.values())
man = list(man.values())

for i in range(len(woman)):
    if woman[i] % k == 0:
        rooms += woman[i]//k
    else:
        rooms += woman[i]//k + 1
for i in range(len(man)):
    if man[i] % k == 0:
        rooms += man[i]//k
    else:
        rooms += man[i]//k + 1

print(rooms)