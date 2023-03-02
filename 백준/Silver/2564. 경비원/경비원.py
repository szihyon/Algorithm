# 하나의 시계로 간주하고 풀이
# 위의 왼쪽 좌표부터 시계방향으로 숫자가 1증가하는 것으로 새로 위치값 설정 후 계산
# 시계방향과 반시계방향의 움직임을 모두 계산 후 더 작은 값을 변수에 할당 후 출력 
width, height = map(int, input().split())
n = int(input())
lst = []
for i in range(n):
    lst.append(map(int, input().split()))
g_dir, guard = map(int, input().split())
if g_dir == 2:
    guard = width + height + (width - guard)
elif g_dir == 3:
    guard = width * 2 + height + (height - guard)
elif g_dir == 4:
    guard = width + guard

sum_val = 0
for i in range(n):
    s_dir, store = lst[i]

    if s_dir == 2:
        store = width + height + (width - store)
    elif s_dir == 3:
        store = width*2 + height + (height- store)
    elif s_dir == 4:
        store = width + store

    if (width+height)*2 - abs(guard - store) > abs(guard - store):
        sum_val += abs(guard - store)
    else:
        sum_val += ((width+height)*2 - abs(guard - store))

print(sum_val)
