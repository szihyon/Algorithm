width, height = map(int, input().split())   # 종이의 크기 입력받기
n = int(input())

width_lst = [0] # 제일 앞에 0번 인덱스 적어주기
height_lst = [0]

for i in range(n):
    a, b = map(int, input().split())
    if a == 1:  # 세로로 자르면 가로 인덱스에 추가 (가로가 2, 3, 4... 조각으로 나뉘니까)
        width_lst.append(b)
    else:   # 가로로 자르면 세로 인덱스에 추가
        height_lst.append(b)

width_lst.append(width)   # 제일 뒤에 마지막 인덱스 적어주기
height_lst.append(height)
width_lst.sort()    # 오름차순 정렬하기 (인덱스 순서대로)
height_lst.sort()

width_max = 0
height_max = 0
for i in range(len(width_lst)-1):   # 정렬된 인덱스들의 앞뒤차이 중 최대값 구하기
    if width_lst[i+1] - width_lst[i] > width_max:
        width_max = width_lst[i+1] - width_lst[i]

for i in range(len(height_lst)-1):
    if height_lst[i+1] - height_lst[i] > height_max:
        height_max = height_lst[i+1] - height_lst[i]

print((width_max)*(height_max))