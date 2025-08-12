import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def dfs(node, parent, dist):
    max_dist = dist
    for next_node, weight in graph[node]:
        if next_node != parent:  # visit 배열 대신 parent로 처리
            max_dist = max(max_dist, dfs(next_node, node, dist + weight))
    return max_dist

print(dfs(1, -1, 0))