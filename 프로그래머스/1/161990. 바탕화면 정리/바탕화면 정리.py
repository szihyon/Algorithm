def solution(wallpaper):
    answer = []
    h = len(wallpaper)
    w = len(wallpaper[0])
    y_lst = []
    x_lst = []
    
    # 가로 탐색 
    for i in range(h):
        for j in range(w):
            if wallpaper[i][j] == "#":
                y_lst.append(i)
                
    # 세로 탐색 
    for i in range(w):
        for j in range(h):
            if wallpaper[j][i] == "#":
                x_lst.append(i)
    lux = x_lst[0]
    rdx = x_lst[-1]
    luy = y_lst[0]
    rdy = y_lst[-1]
    answer = [luy, lux, rdy+1, rdx+1]
    return answer