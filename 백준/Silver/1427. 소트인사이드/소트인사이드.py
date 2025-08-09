sort_list = list(map(int,input()))
size = len(sort_list)

for i in range(0,size-1):
    for j in range(i+1, size):
        if sort_list[i]<sort_list[j]:
            temp = sort_list[i]
            sort_list[i] = sort_list[j]
            sort_list[j] = temp


print("".join(map(str,sort_list)))