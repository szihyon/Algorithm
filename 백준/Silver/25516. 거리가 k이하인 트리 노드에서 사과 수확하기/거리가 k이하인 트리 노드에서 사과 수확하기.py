import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이 충분히 늘리기
input = sys.stdin.readline

n, k = map(int, input().split())
g = [[] for _ in range(n)]

# 트리 간선 입력
for _ in range(n - 1):
    p, c = map(int, input().split())
    g[p].append(c)

# 각 노드의 사과 여부
apples = list(map(int, input().split()))

def dfs(node, depth):
    if depth > k:  # k 초과면 더 내려가지 않음
        return 0
    total = apples[node]  # 현재 노드 사과 수(0 또는 1)
    for child in g[node]:
        total += dfs(child, depth + 1)
    return total

print(dfs(0, 0))
