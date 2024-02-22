def solution(num_list):
    odd_lst = []
    even_lst = []
    
    for num in num_list:
        if num % 2 == 0:
            even_lst.append(num)
        else:
            odd_lst.append(num)
    
    odd_num = ''
    for odd in odd_lst:    
        odd_num += str(odd)
        
    even_num = ''
    for even in even_lst:    
        even_num += str(even)
    
    answer = int(odd_num) + int(even_num)
    
    return answer