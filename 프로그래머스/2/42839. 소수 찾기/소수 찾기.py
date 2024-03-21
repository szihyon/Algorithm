def solution(numbers):
    answer = 0
    numbers = list(numbers)
    num_lst = []
    def dfs(level, path):
        num_lst.append(path)
        for i in range(len(numbers)):
            if level == 0 and numbers[i] == '0': continue
            if used[i] == 1: continue
            used[i] = 1
            dfs(level+1, path+numbers[i])
            used[i] = 0
    
    used = [0]*len(numbers)
    dfs(0, '')
    num_lst = list(map(int, set(num_lst[1:])))
    for num in num_lst:
        if num < 2:  
            continue
        is_prime = True  
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False  
                break
        if is_prime:  
            answer += 1
    return answer