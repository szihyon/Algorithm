def solution(board, h, w):
    answer = 0
    n = len(board)
    
    dh = [0, 1, -1, 0]
    dw = [1, 0, 0, -1]
    for i in range(4):
        if h+dh[i]<0 or h+dh[i]>n-1 or w+dw[i]<0 or w+dw[i]>n-1: continue
        h_check = h+dh[i]
        w_check = w+dw[i]
        if board[h_check][w_check] == board[h][w]:
            answer += 1

    return answer