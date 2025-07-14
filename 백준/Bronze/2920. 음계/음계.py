n_list = list(map(int,input().split()))


def check(n_list):
    sum = 0
    for n in range(7):
        if(n_list[n]< n_list[n+1]):
            sum += 1
        else:
            sum -= 1
            
        if (abs(sum)!=(n+1)):
            return "mixed"
    if sum <0:
        return "descending"
    else:
        return "ascending"
    
print(check(n_list))