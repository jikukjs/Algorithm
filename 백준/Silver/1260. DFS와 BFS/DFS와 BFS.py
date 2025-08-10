from collections import deque

def DFS(S):
    result_1.append(S)
    visit_1[S] = 1

    for node in sorted(graph[S]):
        if visit_1[node]!= 1:
            DFS(node)
        

def BFS(S):
    visit_2[S]=1
    Q.append(S)
    while Q:
        s = Q.popleft()
        result_2.append(s)
        
        for node in sorted(graph[s]):
            if visit_2[node]!=1:
                Q.append(node)
                visit_2[node]=1

N, M, V = map(int,input().split())
graph=[[]for _ in range(N+1)]
visit_1 = [0]*(N+1)
visit_2 = [0]*(N+1)
result_1 = []
result_2 = []
Q = deque()

for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

DFS(V)
BFS(V)


print(" ".join(map(str,result_1)))
print(" ".join(map(str,result_2)))
