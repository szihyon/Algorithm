from collections import Counter

n = int(input())
n_lst = list(map(int, input().split()))
n_dict = Counter(n_lst)

m = int(input())
m_lst = list(map(int, input().split()))

for key in m_lst:
    print(n_dict[key], end=' ')