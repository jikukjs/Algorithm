from collections import deque

def solution(maps):
    answer = 0
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    queue = deque()
    row = len(maps)
    col = len(maps[0])
    
    def BFS(x,y):
        queue.append((x,y))
        maps[x][y] = 2
        while(queue):
            x, y = queue.popleft()
            for i in range(4):
                cx = x+dx[i]
                cy = y+dy[i]
                
                if cx <0 or cy < 0 or cx >= row or cy >= col:
                    continue
                if maps[cx][cy] != 0:
                    if maps[cx][cy] == 1:
                        maps[cx][cy] = maps[x][y] +1
                        queue.append((cx,cy))
                        continue
                    if maps[cx][cy] > maps[x][y]+1:
                        maps[cx][cy] = maps[x][y] +1
                        queue.append((cx,cy))  
    BFS(0,0)
    
    if maps[row-1][col-1] == 1:
        return -1
    else:
        return maps[row-1][col-1]-1
    