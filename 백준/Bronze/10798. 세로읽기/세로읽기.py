S = ['']*5

for i in range(5):
    S[i] = list(input())

maxLen = 0
for s in S:
    if len(s) > maxLen:
        maxLen = len(s)

for s in S:
    if len(s) != maxLen:
        for _ in range(maxLen-len(s)):
            s.append('')
# print(S)

for i in range(maxLen):
    for j in range(5):
        print(S[j][i], end='')