import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    M,N,K = map(int,input().split())

    graph = [[0 for _ in range(M)] for _ in range(N)]
    visit = [[0 for _ in range(M)] for _ in range(N)]
    result = 0

    def DFS(x,y):
        global graph
        global visit

        visit[x][y] = result
        dx = [1,-1,0,0]
        dy = [0,0,1,-1]
        
        for i in range(4):
            cx = x+dx[i]
            cy = y+dy[i]
            
            if cx<0 or cy<0 or cx>=N or cy>=M:
                continue
            
            if visit[cx][cy] ==0 and graph[cx][cy]==1:
                DFS(cx,cy) 

    for _ in range(K):
        x,y = map(int,input().split())
        graph[y][x] = 1
        
    for i in range(N):
        for j in range(M):
            if graph[i][j]==1 and visit[i][j] ==0:
                result +=1 
                DFS(i,j)    
            
    print(result)