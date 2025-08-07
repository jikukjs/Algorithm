from heapq import heappush, heappop
import sys
input = sys.stdin.readline

def pop(heap):
    while len(heap)>0:
        data, id = heappop(heap)
        if not deleted[id] :
            deleted[id]=True
            return data
    return None

test_case = int(input())

for _ in range(test_case) :
    N = int(input())
    Min_heap = []
    Max_heap = [] 
    cnt = 0  
    deleted = [False]*(N+1)

    for _ in range(N):
        i,n = input().split()
        n = int(n)
        if i == 'D':
            if n == -1:
                pop(Min_heap)
            elif n == 1:
                pop(Max_heap)

        elif i == 'I':
            heappush(Max_heap,(-n,cnt))
            heappush(Min_heap,(n,cnt))
            cnt+=1
    Max_value = pop(Max_heap)
     
    if Max_value == None:  
        print("EMPTY")
    else :
        heappush(Min_heap,(-Max_value,cnt))
        print(-Max_value,pop(Min_heap))