def solution(players, m, k):
    answer = 0
    now_server = [0]*24
    cnt = [0]*24
    
    for i in range(len(players)):
        player = players[i]
        
        if player >= (now_server[i]+1)*m:
            add_server = (player-now_server[i]*m)//m
            
            cnt[i] += add_server
            for j in range(i, i+k):
                if(j > 23):
                    break
                
                now_server[j] += add_server
    answer = sum(cnt)
    return answer