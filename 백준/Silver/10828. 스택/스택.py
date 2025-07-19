import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline

N = int(input())
result =[]
for i in range (N):
    arr = list(input().split())
    if arr[0] == 'push':
        result.append(arr[1])
        continue
    if arr[0] == "top":
        if len(result) == 0:
            print(-1)
        else:
            print(result[-1])
        continue
    if arr[0] == 'size':
        print(len(result))
        continue
    if arr[0] == 'empty':
        if len(result) == 0:
            print(1)
        else:
            print(0)
        continue
    if arr[0] == 'pop':
        if len(result) == 0:
            print(-1)
        else:
            a = result.pop()
            print(a)
        continue