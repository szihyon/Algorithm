s = list(input())
n = len(s)
s_dict = dict()
answer = 0

# 주어진 알파벳 딕셔너리 만들기
for a in s:
    if a in s_dict:
        s_dict[a] += 1
    else:
        s_dict[a] = 1

# dfs 함수
def dfs(level, lucky_str):
    global answer
		# 주어진 알파벳들을 전부 사용하면 정답+1
    if level == n:
        answer += 1
        return
		
		# 알파벳을 딕셔너리에서 하나씩 꺼내기 
    for a in s_dict:
				# 알파벳이 남아있지 않으면 continue
        if s_dict[a] == 0: continue
				# 직전에 사용한 문자와 같으면 continue
        if level > 0 and a == lucky_str[-1]: continue
				# 조건 통과후 알파벳 사용
        s_dict[a] -= 1
        dfs(level+1, lucky_str+a)
        s_dict[a] += 1 # return 후 돌아올 때 다시 +1

dfs(0, '')
print(answer)