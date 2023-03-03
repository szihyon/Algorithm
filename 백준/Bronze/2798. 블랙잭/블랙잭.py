n, m = map(int, input().split())     
card = list(map(int, input().split()))
used = [0]*len(card)
Max_sum = 0

def black(level, sum):
    global Max_sum
    if sum > m:
        return

    if level == 3:
        if sum > Max_sum:
            Max_sum = sum
        return

    for i in range(len(card)):
        if used[i] == 1: continue
        used[i] = 1
        black(level+1, sum + card[i])
        used[i] = 0

black(0, 0)
print(Max_sum)