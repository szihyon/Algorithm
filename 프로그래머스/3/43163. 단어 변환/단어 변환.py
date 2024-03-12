from collections import deque

def solution(begin, target, words):
    answer = 0
    n = len(words)
    n2 = len(words[0])
    used = [0]*n
    
    def bfs(begin):
        q = deque()
        q.append([begin, 0])
        while q:
            now_word, step = q.popleft()
            for i in range(n):
                if used[i] == 1: continue
                cnt = 0
                for j in range(n2):
                    if words[i][j] != now_word[j]:
                        cnt += 1
                if cnt == 1:
                    used[i] = 1
                    q.append([words[i], step+1])
                    if words[i] == target:
                        return step + 1
        return 0    
    answer = bfs(begin)
    return answer