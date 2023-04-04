from collections import deque
# 입력값 받기
m, n, h = map(int, input().split())
# 3차원 배열
lst1 = []
# 3차원 배열을 만들기 위해 사용할 2차원 배열
lst2 = []

# 3차원 리스트 만들기
# h 높이만큼 반복(3차원)
for i in range(h):
    lst2 = []
    # n 세로만큼 반복(2차원)
    # lst2에 2차원 배열을 담고,
    for j in range(n):
        lst2.append(list(map(int, input().split())))
    # 2차원 배열을 lst1에 담는다.
    lst1.append(lst2)

# Queue 생성하기
q = deque()

cnt = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            # 3차원 배열을 탐색해서 익은 토마토(1)가 있으면,
            # 높이, 세로, 가로, 날짜를 한 묶음으로 Queue에 추가하기
            if lst1[i][j][k] == 1:
                q.append((i, j, k, 0))
            # 모든 토마토가 익어있는 상태면 0을 출력해야 하기 때문에, 익지 않은 토마토 개수 세기
            elif lst1[i][j][k] == 0:
                cnt += 1

flag = 1
# 만약 모든 토마토가 익어 있다면(안 익은 토마토 0개), flag 끄고, 0출력하기
if cnt == 0:
    flag = 0
    print(0)


# 만약 flag가 안 꺼져 있다면(안 익은 토마토가 있다면) BFS 실행하기
if flag == 1:
    # 상하좌우앞뒤 배열 생성
    directH = [-1, 1, 0, 0, 0, 0]
    directN = [0, 0, -1, 1, 0, 0]
    directM = [0, 0, 0, 0, -1, 1]

    while q:
        # 높이, 세로, 가로, 날짜를 각각 변수에 담기
        h2, n2, m2, day = q.popleft()

        # 상하좌우앞뒤 탐색하기
        for i in range(6):
            dh = h2 + directH[i]
            dn = n2 + directN[i]
            dm = m2 + directM[i]
            # 범위 벗어나면 continue
            if dm < 0 or dm > m-1 or dn < 0 or dn > n-1 or dh < 0 or dh > h-1:continue
            # 토마토가 없으면(-1) continue
            if lst1[dh][dn][dm] == -1: continue
            # 근처에 안익은 토마토가 있으면 익혀주기(1)
            if lst1[dh][dn][dm] == 0:
                lst1[dh][dn][dm] = 1
                # 토마토 익히고 Queue에 넣어주기, 날짜는 +1
                q.append((dh, dn, dm, day+1))

    # 토마토가 모두 익지 못하는 상황인지 체크
    for i in range(h):
        for j in range(n):
            for k in range(m):
                # 여전히 안익은 토마토가 있다면 flag 끄기
                if lst1[i][j][k] == 0:
                    flag = 0
                    break
            if flag == 0:
                break
        if flag == 0:
            break

    # 이제 안 익은 토마토가 없으면, 마지막으로 익은 토마토의 날짜 출력하기
    if flag == 1:
        print(day)
    # 토마토가 모두 익지 못하는 상황이면 -1 출력하기
    else:
        print(-1)
