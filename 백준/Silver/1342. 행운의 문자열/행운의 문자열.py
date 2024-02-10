s = list(input())
n = len(s)
cnt = dict()
answer = 0

# 주어진 알파벳 딕셔너리 만들기
for i in s:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1


def dfs(level, path):
    global answer
    if level == n:
        answer += 1
        return

    for i in cnt:
        if cnt[i] == 0: continue
        if level > 0 and i == path[-1]: continue
        cnt[i] -= 1
        dfs(level+1, path+i)
        cnt[i] += 1

dfs(0, '')
print(answer)