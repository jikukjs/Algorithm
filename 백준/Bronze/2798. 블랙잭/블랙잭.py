N, M = map(int,input().split())

N_list = list(map(int,input().split()))


def susu(N_list):
    max_n = 0
    for i in range(N-2):
        for j in range(i+1,N-1):
            for k in range(j+1,N):
                sum_n = N_list[i]+N_list[j]+N_list[k]
                if ((sum_n > max_n) & (sum_n < M)):
                    max_n = sum_n
                elif(sum_n == M):
                    max_n = sum_n
                    return max_n
    return max_n

print(susu(N_list))