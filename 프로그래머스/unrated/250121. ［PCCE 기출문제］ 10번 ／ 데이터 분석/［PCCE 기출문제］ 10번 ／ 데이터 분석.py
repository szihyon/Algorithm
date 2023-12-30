def solution(data, ext, val_ext, sort_by):
    answer = []
        
    if ext == "code":
        ext_index = 0
    elif ext == "date":
        ext_index = 1
    elif ext == "maximum":
        ext_index = 2
    else:
        ext_index = 3
        
    if sort_by == "code":
        sort_by_index = 0
    elif sort_by == "date":
        sort_by_index = 1
    elif sort_by == "maximum":
        sort_by_index = 2
    else:
        sort_by_index = 3
        
    for i in range(len(data)):
        print(data[i][ext_index])
        if data[i][ext_index] < val_ext:
            answer.append(data[i])
    
    answer.sort(key=lambda x:x[sort_by_index])	
    return answer