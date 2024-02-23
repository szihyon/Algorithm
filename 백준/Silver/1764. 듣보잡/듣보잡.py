N, M = map(int, input().split())
name_dict ={}
cnt = 0
for _ in range(N):
    name = input()
    if name in name_dict:
        cnt += 1
        name_dict[name] += 1
    else:
        name_dict[name] = 1
for _ in range(M):
    name = input()
    if name in name_dict:
        cnt += 1
        name_dict[name] += 1
    else:
        name_dict[name] = 1
print(cnt)

answer = []
for name in name_dict:
    if name_dict[name] > 1:
        answer.append(name)

answer.sort()
for name in answer:
    print(name)