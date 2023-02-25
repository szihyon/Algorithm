dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    arr = [[0] * n for _ in range(n)]
    # 초기값 설정(초기좌표, 방향)
    x, y, dr = 0, 0, 0
    for cnt in range(1, n * n + 1):
        arr[x][y] = cnt
        # 다음 좌표 계산
        nx, ny = x + dx[dr], y + dy[dr]
        # 이동할 위치가 범위 내 & 비어 있으면 (값이 0이면)
        if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 0:
            x, y = nx, ny
        else:
            dr = (dr + 1) % 4
            x, y = x + dx[dr], y + dy[dr]
    print(f'#{tc}')

    for lst in arr:
        print(*lst)
