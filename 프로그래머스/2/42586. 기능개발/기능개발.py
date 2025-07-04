def solution(progresses, speeds):
    answer = []
    stack = []
    for i in range(len(progresses)):
        day = 0
        remain = 100-progresses[i]
        
        if remain%speeds[i]:
            day = remain//speeds[i]+1
        else:
            day = remain//speeds[i]
        
        if not stack:
            stack.append(day)
            continue
            
        if stack[0] >=day:
            stack.append(stack[0])
        else:
            answer.append(len(stack))
            stack = [day]
    answer.append(len(stack))
    return answer

