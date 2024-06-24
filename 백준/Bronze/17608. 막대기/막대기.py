import sys
input = sys.stdin.readline

N = int(input())
heights = [int(input()) for _ in range(N)]
current_max = heights[-1]
answer = 1
for i in range(len(heights)-1, -1, -1):
    if heights[i] > current_max:
        current_max = heights[i]
        answer += 1
print(answer)