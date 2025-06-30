import heapq
import sys

input = sys.stdin.readline

K, N = map(int, input().split())
heap = []
selected = set()
cnt = 0

n_list = list(map(int, input().split()))

max_value = max(n_list)

for n in n_list:
    heapq.heappush(heap,n)

while(cnt != N):
    cnt+=1
    n = heapq.heappop(heap)
    for i in n_list:
        new = n*i
            
        if len(heap) >= N and max_value < new:
            continue
        if new not in selected:
            selected.add(new)
            max_value = max(max_value, new)
            heapq.heappush(heap, new)
        
print(n)