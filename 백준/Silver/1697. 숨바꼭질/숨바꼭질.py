from collections import deque

import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline
N, K = map(int,input().split())
arr = [0]*100001

queue = deque()

def dsf(x):
    while queue:
        num = queue.popleft()
        dx = [num-1,num+1,2*num]
        for i in dx:
            if i <0 or i>100000 or arr[i]!= 0:
                continue
            if i == K and arr[K]!=0 and arr[K] >arr[num]+1:
                arr[K] = arr[num]+1
                continue
            arr[i] = arr[num]+1
            if i<2*max(N,K):
                queue.append(i)
            

arr[N]=1
queue.append(N)
dsf(N)
print(arr[K]-1)