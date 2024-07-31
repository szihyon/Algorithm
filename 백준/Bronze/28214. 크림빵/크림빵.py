N, K, P = map(int, input().split())
cream = list(map(int, input().split()))
answer = 0

for i in range(0, N*K, K):
    bundle = cream[i:i+K]
    if bundle.count(0) < P:
        answer += 1

print(answer)