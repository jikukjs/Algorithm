from collections import deque


def solution(land):
    

    def BSF(i,j,num):
        lique_q = deque()
        lique_q.append((i,j))
        land[i][j] = num
        cnt = 1
        
        while(lique_q):
            x, y = lique_q.popleft()
            visited[x][y] = 1
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if nx <0 or ny <0 or nx>=row or ny>=col:
                    continue
                if land[nx][ny] ==0:
                    continue
                if land[nx][ny] ==1:
                    if visited[nx][ny]==0:
                        land[x+dx[i]][y+dy[i]] = num
                        visited[nx][ny] = 1
                        cnt+=1
                        lique_q.append((x+dx[i],y+dy[i]))          
        return cnt
    
    row = len(land)  #5
    col = len(land[0]) #8
    answer = 0
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    num = 1
    check_list = [0]
    result = []
    
    visited = [[0 for _ in range(col)] for _ in range(row)]
        
    for i in range(row):
        for j in range(col):
            if land[i][j] == 1 and visited[i][j] == 0:
                cnt = BSF(i,j,num)
                num+=1
                check_list.append(cnt)
          #      print(cnt)
  #  print(land)
  #  print(check_list)
    for j in range(col):
        col_check = set()
        col_sum = 0
        for i in range(row):
            col_check.add(land[i][j])
       # print(col_check)    
        
        for c in col_check:
            col_sum += check_list[c]
        result.append(col_sum)
   # print(result)
    return max(result)