N, K = map(int, input().split())

DP = [[0]*(K+1) for _ in range(N+1)]

for i in range(1,N+1):
    w, v = map(int, input().split())
    
    for j in range(1,K+1):
        if w > j:
            DP[i][j] = DP[i-1][j]
        else:
            DP[i][j] = max(DP[i-1][j], DP[i-1][j-w]+v)
            

print(DP[N][K])
