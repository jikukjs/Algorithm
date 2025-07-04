def solution(n, computers):
    answer = 0
    candidate = set()
    parents = [0]*n
    answer_set = set()
    for i in range(n):
        parents[i] = i
    
    def join(x,y):
        x_p = find(x)
        y_p = find(y)
    
        if x_p!=y_p:
            parents[y_p] = x_p
    
    def find(x):
        if parents[x] != x:
            parents[x] = find(parents[x])

        return parents[x]
        
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] ==1:
                if i<=j :
                    candidate.add((i,j))
                else:
                    candidate.add((j,i))
    
    for can in list(candidate):
        x,y = can[0],can[1]
        
        join(x,y)
    
    for i in range(n):
        answer_set.add(find(parents[i]))
    
    return len(answer_set)