import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))

h_start, h_end = 1, max(trees)  # h 시작과 끝 값

while h_start <= h_end:
    cut = 0
    mid = (h_start + h_end) // 2  # h 중간값

    for tree in trees:
        if tree > mid:
            cut += tree - mid  # h 중간값으로 잘랐을 때 가져갈 수 있는 나무

    if cut < m:  # 가져갈 수 있는 나무가 목표보다 작은 경우
        h_end = mid - 1  # 높이 낮추기 (더 많이 자를 수 있게)
    else:  # 가져갈 수 있는 나무가 목표보다 크거나 같은 경우
        h_start = mid + 1  # 높이 높이기 (더 적게 자를 수 있게)

print(h_end)