N, M = map(int,input().split())

graph = [[] for _ in range(N+1)] 

def DSF(S):

    for n,v in graph[S]:
        if visit[n]==0:
            visit[n]=1
            dis[n] = dis[S] + v
            DSF(n)
            
for _ in range(N-1):
    a,b,v = map(int,input().split())
    graph[a].append((b,v))
    graph[b].append((a,v))

for _ in range(M):
    visit= [0]*(N+1)
    dis = [-1]*(N+1)
    s,e = map(int,input().split())
    visit[s]=1
    dis[s] = 0
    DSF(s)
    print(dis[e])
    