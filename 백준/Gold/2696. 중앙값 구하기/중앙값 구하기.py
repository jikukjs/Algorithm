import heapq
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):

    M = int(input())
    top_list =[]
    bottom_list = []
    answer = []

    num_list = []
    for i in range(M//10+1):
        num_list.extend(list(map(int,input().split())))

    top_list.append(num_list[0])
    answer.append(num_list[0])

    for i in range(1, len(num_list)):
        now_middle = heapq.heappop(top_list) 
        if num_list[i] < now_middle:
            heapq.heappush(bottom_list, -1*num_list[i])
        else:
            heapq.heappush(top_list, num_list[i])
        heapq.heappush(top_list, now_middle)
        
        if i%2 ==0:
            if len(bottom_list) >= len(top_list):
                heapq.heappush(top_list, -1*heapq.heappop(bottom_list))
            
            elif len(top_list) > len(bottom_list)+1:
                heapq.heappush(bottom_list, -1*heapq.heappop(top_list))
            
            new_middle = heapq.heappop(top_list)
            answer.append(new_middle)
            heapq.heappush(top_list,new_middle)

    print(len(answer))
    for i in range(len(answer)):
        print(answer[i], end=" ")
        if (i+1)%10 ==0:
            print()