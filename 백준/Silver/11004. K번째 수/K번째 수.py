import sys

input = sys.stdin.readline

def merge_sort(n_list):
    if len(n_list) <= 1:
        return n_list
    mid = len(n_list)//2
    left = merge_sort(n_list[:mid])
    right = merge_sort(n_list[mid:])
    
    i, j, k = 0,0,0
    
    while(i<len(left)) and (j<len(right)):
        if left[i]> right[j]:
            n_list[k] = right[j]
            j+=1
        else:
            n_list[k] = left[i]
            i+=1
        k+=1
    
    if i == len(left):
        while(j<len(right)):
            n_list[k] = right[j]
            j+=1
            k+=1
    elif j == len(right):
        while(i<len(left)):
            n_list[k] = left[i]
            i+=1
            k+=1

    return n_list

N,K = map(int,input().split())

n_list = list(map(int,input().split()))

n_list = merge_sort(n_list)
print(n_list[K-1])
