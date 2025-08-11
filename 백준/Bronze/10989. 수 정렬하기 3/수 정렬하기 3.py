import sys
N = int(sys.stdin.readline())

#N = int(input())

n_list = [0]*10001

for i in range(N):
    #num = int(input())
    num = int(sys.stdin.readline())
    n_list[num]+=1
    
for i in range(len(n_list)):
    for j in range(n_list[i]):
        print(i)