
max = 0
for i in range(5):
    score_List = list(map(int, input().split()))
    score = sum(score_List)
    if max < score:
        max = score
        max_inx = i
print(max_inx+1, max)