import math

def solution(n, w, num):
    answer = 0
    
    total_layers = math.ceil(n / w)
    box = [[-1]*w for _ in range(total_layers)]
    
    #택배 상자 쌓기
    for h in range(total_layers):  #층만큼
        n2 = h * w + 1
        if h%2 == 0: #짝수층 
            for j in range(w):  #정방향으로 숫자 채우기
                if n2 <= n:  # 범위 체크 추가!!
                    box[h][j] = n2
                n2 += 1
        else: #홀수층 
            for j in range(w-1, -1, -1):  #역방향으로 숫자 채우기
                if n2 <= n:  # 범위 체크 추가!!
                    box[h][j] = n2
                n2 += 1
    
    #택배 찾기
    for i in range(total_layers):
        for j in range(w):
            if box[i][j] == num:
                if box[total_layers-1][j] != -1:
                    answer = total_layers - i
                else:
                    answer = total_layers -i -1
            
    return answer