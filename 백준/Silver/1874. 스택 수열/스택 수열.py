from collections import deque
import sys

input = sys.stdin.readline

N = int(input())

kjs =[]
answer = []
num_list =[]
cnt = 1

for i in range(N):
    kjs.append(int(input()))

for i in range(N):
    num = kjs[i]
    
    while(cnt <= num):
        num_list.append(cnt)
        cnt+=1
        answer.append("+")
    
    a = num_list.pop()
    if num == a:
        answer.append("-")
    else:
        answer = []
        answer.append("NO")
        break
    
for a in answer:
    print(a)
