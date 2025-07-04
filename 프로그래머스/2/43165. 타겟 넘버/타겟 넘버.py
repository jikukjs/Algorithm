from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque()
    def BSF(inx,answer):
        queue.append((numbers[inx],inx))
        queue.append((-1*numbers[inx],inx))
                
        while queue:
            sum_result, inx = queue.popleft()
            inx+=1
            if inx==len(numbers) and sum_result == target:
                answer +=1
                continue
            
            if inx < len(numbers):
                queue.append((sum_result+numbers[inx], inx))
                queue.append((sum_result-numbers[inx], inx))
        return answer
            
    answer = BSF(0,answer)
    
    return answer