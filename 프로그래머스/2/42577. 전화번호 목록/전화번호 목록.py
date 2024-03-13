def solution(phone_book):
    phone_book.sort()  # 전화번호 목록을 사전 순으로 정렬
    for i in range(len(phone_book) - 1):
        # 정렬된 목록에서 연속된 두 번호만 비교하여,
        # 앞 번호가 뒤 번호의 접두어인 경우 False를 반환
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return True
