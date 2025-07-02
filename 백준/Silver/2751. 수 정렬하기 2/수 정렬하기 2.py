import sys
input = sys.stdin.readline

N = int(input())

n_list = []

for _ in range(N):
    n_list.append(int(input()))
    
n_list.sort()

for i in n_list:
    print(i)