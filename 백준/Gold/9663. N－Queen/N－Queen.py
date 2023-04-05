n = int(input())

# dat, rup, rdown은 열, 우상향 대각선, 우하향 대각선 각 위치의 중복을 체크해줄 배열
dat = [0] * n
rup = [0] * (2*n-1)
rdown = [0] * (2*n-1)
cnt = 0

def func(level):
    global cnt
    # 마지막 행까지 도달하면 카운트
    if level == n:
        cnt += 1
        return
        
    for i in range(n):
    	# 열 중복체크. 1이면 continue
        # dat[열]
        if dat[i] == 1:
            continue
        # 우상향 대각선 중복체크, rup[행+열]
        if rup[level + i] == 1: continue
        # 우하향 대각선 중복체크, rdown[(행-열)+(n-1)]
        if rdown[(level - i) + (n-1)] == 1: continue
        
        # 모두 중복이 아니라면 1체크 후, 
        rup[level + i] = 1
        rdown[(level - i) + (n-1)] = 1
        dat[i] = 1
        
        # 다음 행 함수 호출
        func(level + 1)
        
        # return하면 다시 0으로 갱신
        dat[i] = 0
        rup[level + i] = 0
        rdown[(level - i) + (n-1)] = 0

func(0)
print(cnt)
