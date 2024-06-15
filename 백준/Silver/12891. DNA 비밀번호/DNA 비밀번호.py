N, L = map(int, input().split())
DNA = list(input())
CNT = list(map(int, input().split()))
start = 0
end = L-1
first_dna = DNA[start:end+1]
temp_cnt = [first_dna.count('A'), first_dna.count('C'), first_dna.count('G'), first_dna.count('T')]
answer = 0

while end < N:
    if temp_cnt[0] >= CNT[0] and temp_cnt[1] >= CNT[1] and temp_cnt[2] >= CNT[2] and temp_cnt[3] >= CNT[3]:
        answer += 1

    if end == N-1:
        break

    if DNA[start] == 'A':
        temp_cnt[0] -= 1
    elif DNA[start] == 'C':
        temp_cnt[1] -= 1
    elif DNA[start] == 'G':
        temp_cnt[2] -= 1
    else:
        temp_cnt[3] -= 1

    if DNA[end+1] == 'A':
        temp_cnt[0] += 1
    elif DNA[end+1] == 'C':
        temp_cnt[1] += 1
    elif DNA[end+1] == 'G':
        temp_cnt[2] += 1
    else:
        temp_cnt[3] += 1

    start += 1
    end += 1

print(answer)