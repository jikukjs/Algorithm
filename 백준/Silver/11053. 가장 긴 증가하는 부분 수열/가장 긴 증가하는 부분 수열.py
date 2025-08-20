N = int(input())
DP = [1]*(N+1)

N_list = list(map(int,input().split()))

for i in range(1, N+1):
    num = N_list[i-1]
    if i == 1:
        continue
    for j in range(1,i):
        if N_list[j-1] < num:
            DP[i] = max(DP[i], DP[j]+1)
    
       
print(max(DP))
    