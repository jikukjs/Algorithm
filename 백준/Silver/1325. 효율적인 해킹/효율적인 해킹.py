from collections import deque

def BFS(S):
    cnt = 1
    Q = deque()
    Q.append(S)
    visit = [0]*(N+1)
    visit[S] = 1
    
    while Q:
        n = Q.popleft()
        
        for i in graph[n]:
            if visit[i] == 0:
                Q.append(i) 
                visit[i] = 1
                cnt+=1

    return cnt

N, M = map(int,input().split())

graph = [[] for _ in range(N+1)]
result = []
max_v = 0

for _ in range(M):
    a,b = map(int,input().split())
    graph[b].append(a)
    
for i in range(1,N+1):
    
    cnt = BFS(i)
    if cnt > max_v:
        result = [i]
        max_v = cnt
    elif cnt == max_v:
        result.append(i)

for i in result:
    print(i, end=" ")