def solution(schedules, timelogs, startday):
    answer = 0
    result = []
    
    workday = [1,2,3,4,5]
    
    member_num = len(schedules)
    
    for i in range(member_num):
        score = 0
        std_time = 0
        cnt = 0
        setting_time = schedules[i]
        setting_hour = setting_time//100
        setting_min = schedules[i] % 100
        if setting_min >= 50:
            std_time = (setting_hour+1)*100 + ((setting_min+10)%60)
        else :
            std_time = setting_time + 10
            
        timelog = timelogs[i]
        
        
        for j in range(7):
            if startday > 7:
                startday = startday%7
            
            if startday in workday:
                if timelog[j] <= std_time:
                    cnt +=1
            startday +=1
        if  cnt == 5:
            answer +=1
            
        
    return answer