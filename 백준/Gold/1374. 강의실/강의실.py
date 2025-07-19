import heapq
import sys

input = sys.stdin.readline


N = int(input())

cources = []
end_cource = 0
cnt = 0
heap = []

for _ in range(N):
    cource = list(map(int, input().split()))
    heapq.heappush(cources, (cource[1], cource[2]))

while cources:
    n_start, n_end = heapq.heappop(cources)
    
    # 첫 강의 설정
    if cnt == 0:
        cnt+=1
        heapq.heappush(heap, n_end)
        continue
    
    # 두번쨰 강의부터 설정
    end = heapq.heappop(heap)
    
    if n_start < end:
        heapq.heappush(heap, n_end)
        heapq.heappush(heap, end)
        cnt+=1

    else:
        heapq.heappush(heap, n_end)
        
print(cnt)
