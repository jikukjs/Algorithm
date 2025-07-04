def solution(arr):
    answer = []
    for n in arr:
        if not answer:
            answer.append(n)
            continue
        pre = answer[-1]
        if n == pre:
            continue
        else:
            answer.append(n)
        
    return answer