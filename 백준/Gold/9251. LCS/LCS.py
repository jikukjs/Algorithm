a_List = input()
b_List = input()

DP = [[0]*(len(a_List)+1) for _ in range(len(b_List)+1)]

for i in range(len(b_List)):
    for j in range(len(a_List)):
        if b_List[i]== a_List[j]:
            DP[i+1][j+1]= DP[i][j]+1
        else:
            DP[i+1][j+1] = max(DP[i+1][j], DP[i][j+1])
            
print(DP[len(b_List)][len(a_List)])
      
