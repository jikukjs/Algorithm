import sys

input = sys.stdin.readline

sys.setrecursionlimit(int(1e5))

def DFS(x,y,c):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    for i in range(4):
        cx = x + dx[i]
        cy = y + dy[i]

        if cx <0 or cy < 0 or cx>=N or cy >=N:
            continue
        
        if c == 'R': 
            if graph[cx][cy]=='R' and visit[cx][cy] == 0:
                visit[cx][cy] =1
                DFS(cx,cy,graph[cx][cy])
        
        elif c == 'G':
            if graph[cx][cy]=='G' and visit[cx][cy] == 0:
                visit[cx][cy] =1
                DFS(cx,cy,graph[cx][cy])
        
        else:
            if graph[cx][cy]=='B' and visit[cx][cy] == 0:
                visit[cx][cy] =1
                DFS(cx,cy,graph[cx][cy])

N = int(input())

graph=[]
visit = [[0]*N for _ in range(N)]

for _ in range(N):
    n_l = list(input())
    graph.append(n_l)
    
cnt=0
for i in range(N):
    for j in range(N):
        if visit[i][j]==0:
            cnt+=1
            DFS(i,j,graph[i][j])

visit = [[0]*N for _ in range(N)]
        
n_cnt=0    

for i in range(len(graph)):
    for j in range(len(graph[i])):
        if graph[i][j] == "G":
            graph[i][j] = "R"

for i in range(N):
    for j in range(N):
        if visit[i][j]==0:
            n_cnt+=1
            DFS(i,j,graph[i][j])    

print(cnt,n_cnt)         