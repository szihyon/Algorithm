l, c = map(int, input().split())
st = input().split()
st.sort()
vowel = ['a', 'e', 'i', 'o', 'u']

# 모음이 1개 이상 l-2개 이하

def dfs(level, start):
    if level == l:
        cnt = 0
        for i in range(len(vowel)):
            if vowel[i] in path:
                cnt += 1
        if 1 <= cnt <= l-2:
            print(*path, sep='')
        return

    for i in range(start, len(st)):
        if used[i] == 1: continue
        used[i] = 1
        path[level] = st[i]
        dfs(level + 1, i+1)
        used[i] = 0

used = [0] * len(st)
path = [0] * l
dfs(0, 0)