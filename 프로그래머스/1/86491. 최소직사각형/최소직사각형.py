def solution(sizes):
    answer = 0
    
    # 각 리스트에서 큰 값이 앞에 오도록 정렬
    for size in sizes:
        size.sort(reverse=True)
    
    # 0번 인덱스 중에서 가장 큰 값 고르기
    sizes.sort(key=lambda x:-x[0])
    val1 = sizes[0][0]
    
    # 1번 인덱스 중에서 가장 큰 값 고르기
    sizes.sort(key=lambda x:-x[1])
    val2 = sizes[0][1]
    
    answer = val1 * val2
    
    return answer