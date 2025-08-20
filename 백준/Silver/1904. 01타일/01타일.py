def func(num):
    tile_list = [0 for i in range(1000000)]
    tile_list[0] = 1
    tile_list[1] = 2

    for i in range(2,num):
        tile_list[i] = (tile_list[i-1]+tile_list[i-2])%15746

    return tile_list[num-1]
        
num = int(input()) 
print(func(num))