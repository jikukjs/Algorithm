test_case = int(input())

for i in range(test_case):
    num, find = list(map(int,input().split()))
    queue = list(map(int,input().split()))
    queue = [(n,idx) for idx,n in enumerate(queue)]

    cnt = 0
    while True:
        if queue[0][0] == max(queue, key = lambda x:x[0] )[0]:
            cnt += 1
            if queue[0][1] == find:
                print(cnt)
                break
            else :
                queue.pop(0)
        else :
            queue.append(queue.pop(0))
