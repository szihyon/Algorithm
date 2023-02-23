# 입력받은 숫자들 몇 개를 뽑아서 더했을 때 값이 10-20인 경우
# 조합(순서 상관 없이 중복되지 않게)
# 입력값 5 4 3 9 1
st = list(map(int, input().split()))
cnt = 0
path = [0]*5    # 최대 크기 5
used = [0]*len(st)  # st에서 사용된 원소를 체크함으로써 중복사용 방지

def abc(level, sum_val):
    # print('level', level, 'used', used, 'path', path) 디버깅용 코드
    global cnt

    if 10 <= sum_val <= 20:   # 10~20사이의 값이 되었다고 return하면 안 됨. 20보다 작고 더 큰 수가 있을 수도 있음
        cnt += 1              # 10~20사의 값 count

    if sum_val > 20:    # 20이상은 더 이상 탐색하지 않음
        return

    if level == 5:  # 숫자는 최대 5가지를 뽑을 수 있음 
        return

    for i in range(len(st)):
        if level > 0 and path[level-1] > st[i]: continue    # 중복을 제거하는 코드 
                                                            # ex) 12345, 12435, 54321 등 동일한 조합을 모두 카운트하기 때문에 12345하나만 남겨놓는 것
        if used[i] == 0:    # 아직 사용하지 않은 숫자를 넣어주기
            path[level] = st[i] # 현재 위치(level)에 할당 
            used[i] = 1 # 방금 할당하며 사용했으니 1로 체크
            abc(level+1, sum_val + st[i])   # 다음 위치(level)로 이동하고, 방금 고른 원소 더하면서 재귀
            path[level] = ''    # 돌아오는 길에 path를 초기화해주지 않으면, 덮어씌워지는 문제 발생
                                # 만약 숫자들이 모두 level5까지 간다면 초기화할 필요가 없지만, 
                                # level5까지 도달하지 않고 return하는 값들이 있기 때문에 초기화 필수
            used[i] = 0 # 돌아오는 길에 스위치 꺼주기 

abc(0, 0)   # 시작점
print(cnt)




# 두번째 방법
# #st = list(map(int, input().split()))
# st= [5, 4, 3, 9, 1]
# cnt = 0
#
# def abc(level, sum_val,results=[]):   # 세번째 매개변수는 디버깅용
#     # print(level,sum_val,results) 디버깅용 코드
#     global cnt
#     if sum_val>20:
#         return
#     if 10 <= sum_val + st[level] <= 20:
#         cnt += 1
#         print(results+[st[level]])
#
#     if level == 4:
#         return
#
#     abc(level+1, sum_val + st[level], results+[st[level]])
#     abc(level+1, sum_val, results)
#
# abc(0, 0, [])
# print(cnt)
