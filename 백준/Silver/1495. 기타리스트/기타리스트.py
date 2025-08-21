N, S, M = map(int,input().split())

V = list(map(int,input().split()))

DP = [[0]*(M+1) for _ in range(N+1)]

for i in range(len(DP)-1):
    if i == 0:
        DP[i][S]=1

    for j in range(len(DP[0])):
        if DP[i][j] ==1:
            p_num = j+V[i]
            m_num = j-V[i]
            if p_num >= 0 and p_num<=M:
                DP[i+1][p_num]=1
            if m_num >= 0 and m_num<=M:
                DP[i+1][m_num]=1

result = -1
for i in range(M+1):
    if DP[-1][i] ==1:
        result = i
    
print(result)
    