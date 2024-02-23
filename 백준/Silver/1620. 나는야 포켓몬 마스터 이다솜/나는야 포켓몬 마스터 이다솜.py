N, M = map(int, input().split())
name_to_index = {}
index_to_name = {}

for i in range(1, N+1):
    name = input().strip()
    name_to_index[name] = i
    index_to_name[i] = name

for _ in range(M):
    query = input().strip()
    if query.isdigit():  # 숫자를 입력받았다면
        print(index_to_name[int(query)])
    else:  # 문자를 입력받았다면
        print(name_to_index[query])
