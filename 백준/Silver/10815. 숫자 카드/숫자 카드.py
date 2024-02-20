N = int(input())
n_lst = list(map(int, input().split()))
n_lst.sort()
M = int(input())
m_lst = list(map(int, input().split()))

def check(find_num):
    start = 0
    end = N - 1

    while start <= end:
        mid = (start + end) // 2

        if find_num == n_lst[mid]:
           return 1
        elif find_num > n_lst[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return 0

for i in range(M):
    print(check(m_lst[i]), end=' ')