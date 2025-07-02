def solution(info, n, m):
    global answer 
    answer = 120
    
    
    selected = set((0,0,0))
    
    def DSF(i,a,b):
        global answer 
        selected.add((i,a,b))
        
        if a>=answer or a >= n or b>=m:
            return 
        
        if i == len(info) and a < answer:
            answer = a
            return 
    
        if (i+1,a,b+info[i][1]) not in selected:
            
            DSF(i+1,a,b+info[i][1])
            
        if (i+1,a+info[i][0],b) not in selected:
            DSF(i+1,a+info[i][0],b)
            
    DSF(0,0,0)
    
    if answer == 120:
        return -1
    
    return answer