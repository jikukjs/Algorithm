import heapq
import sys
N = int(input())
heap = []

for _ in range(N):
    operation = int(sys.stdin.readline())
    
    if operation:
        heapq.heappush(heap,(abs(operation),operation))
    else:
        if heap:
            print(heapq.heappop(heap)[1])
        else :
            print(0)