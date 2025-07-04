def solution(phone_book):
    answer = True
    hashs = {}
    for phone in phone_book:
        hashs[phone] = 1
    
    
    for phone in phone_book:
        arr = ""
        for n in phone:
            arr+=n
            if arr in hashs and arr != phone:
                return False
    return answer