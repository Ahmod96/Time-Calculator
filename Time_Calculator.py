def add_time(start, duration, day = ''):
    day = day.capitalize()
    day_list = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    next_day = '(next day)'
    day_later = '({} days later)'
    
    start_split = start.split()
    start_time = start_split[0].split(':')
    duration_split = duration.split(':')
    
    if (int(duration_split[0])*60 + int(duration_split[1])) + (int(start_time[0])*60 + int(start_time[1])) <= 12*60 - 1:
        
        minute = str(int(start_time[1]) + int(duration_split[1]))
        hour = str(int(start_time[0]) + int(duration_split[0]))
        
        if int(minute) >= 60:
            hour = str(int(hour) + int(minute)//60)
        if int(minute) >= 60:
            minute = str(int(minute)%60)
        if start_split[1] == 'PM':
            meridean = 'PM'
        else:
            meridean = 'AM'
        if day == '':
            minute_tens =str(int(minute)//10)
            minute_units = str(int(minute)%10)
            new_time = hour+':'+minute_tens+minute_units+' '+meridean
        else:
            minute_tens =str(int(minute)//10)
            minute_units = str(int(minute)%10)
            new_time = hour+':'+minute_tens+minute_units+' '+meridean+', '+day

    if (int(duration_split[0])*60 + int(duration_split[1])) + (int(start_time[0])*60 + int(start_time[1])) == 12*60:
        
        minute = str(int(start_time[1]) + int(duration_split[1]))
        hour = str(int(start_time[0]) + int(duration_split[0]) +  int(minute)//60)
        
        if start_split[1] == 'AM':
            meridean = 'PM'
            minute = str(int(minute)%60)
            minute_tens =str(int(minute)//10)
            minute_units = str(int(minute)%10)
            if day == '':
                new_time = hour+':'+minute_tens+minute_units+' '+meridean
            else:
                new_time = hour+':'+minute_tens+minute_units+' '+meridean+' '+day
                
        if start_split[1] == 'PM':
            meridean = 'AM'
            minute = str(int(minute)%60)
            minute_tens =str(int(minute)//10)
            minute_units = str(int(minute)%10)
            if day == '':
                new_time = hour+':'+minute_tens+minute_units+' '+meridean+' '+next_day 
            else:
                if day_list.index(day) <= 5:
                    day_index = day_list.index(day) + 1
                else:
                    day_index = day_list.index(day)*0

                new_time = hour+':'+minute_tens+minute_units+' '+meridean+' '+day_list[day_index]+' '+next_day
        
    if (int(duration_split[0])*60 + int(duration_split[1])) + (int(start_time[0])*60 + int(start_time[1])) > 12*60:
        
        current_time_mins = int(start_time[0])*60 + int(start_time[1])
        time_complete_mer = 12*60 - current_time_mins
        duration_mins = int(duration_split[0])*60 + int(duration_split[1])
        
        if duration_mins >= time_complete_mer and start_split[1] == 'PM':
            meridean = 'AM'
        if duration_mins >= time_complete_mer and start_split[1] == 'AM':
            meridean = 'PM'
        
        mins_left = duration_mins - time_complete_mer    #mins left after change of first meridean
        hours_left = mins_left/60   #hourours left after change of first meridean
        num_meridean_change = hours_left//12  #no of meridean change possible after thoure first one
        whole_hour = mins_left//60  #whourole no of hourours left after change of first meridean
        whole_min = mins_left%60   #whourole no of mins left after change of first meridean
        even_odd_check = num_meridean_change%2    #to choureck if num_meridean_change is even or odd
        
        if num_meridean_change == 0 and meridean == 'AM':
            minute = str(whole_min)
            hour = str(whole_hour)
            if int(minute) >= 60:
                hour = str(int(hour) + int(minute)//60)
            if hour == '0':
                    hour = str(12)
            if int(minute) >= 60:
                minute = str(int(minute)%60)
            minute_tens =str(int(minute)//10)
            minute_units = str(int(minute)%10)
            if day == '':
                new_time = hour+':'+minute_tens+minute_units+' '+meridean+' '+next_day
            else:
                if day_list.index(day) <= 5:
                    day_index = day_list.index(day) + 1
                else:
                    day_index = day_list.index(day)*0

                new_time = hour+':'+minute_tens+minute_units+' '+meridean+' '+day_list[day_index]+' '+next_day
        
        if num_meridean_change == 0 and meridean == 'PM':
            minute = str(whole_min)
            hour = str(whole_hour)
            if int(minute) >= 60:
                hour = str(int(hour) + int(minute)//60)
            if hour == '0':
                    hour = str(12)
            if int(minute) >= 60:
                minute = str(int(minute)%60)
            minute_tens =str(int(minute)//10)
            minute_units = str(int(minute)%10)
            if day == '':
                new_time = hour+':'+minute_tens+minute_units+' '+meridean
            else:
                new_time = hour+':'+minute_tens+minute_units+' '+meridean+' '+day

        
        if num_meridean_change > 0:
            if even_odd_check == 0 and meridean == 'PM':
                meridean = 'PM'
                minute = str(whole_min)
                hour = str(whole_hour - (round(12*num_meridean_change)))
                if int(minute) >= 60:
                    hour = str(int(hour) + int(minute)//60)
                if hour == '0':
                    hour = str(12)
                if int(minute) >= 60:
                    minute = str(int(minute)%60)
                num_day = round(whole_hour/24)

                minute_tens =str(int(minute)//10)
                minute_units = str(int(minute)%10)
                if num_day == 1:
                    if day == '':
                        new_time = hour+':'+minute_tens+minute_units+' '+meridean+' '+next_day
                    else:
                        day_index = day_list.index(day)
                        day_count = 1
                        while day_count <= num_day: 
                            if day_index == 6:
                                day_index = 6*0
                            else:
                                day_index = day_index + 1
                            day_count += 1
                        current_day = day_list[day_index]
                        new_time = hour+':'+minute_tens+minute_units+' '+meridean+' '+current_day+' '+next_day
                else:
                    if day == '':
                        new_time = hour+':'+minute_tens+minute_units+' '+meridean+' '+day_later.format(num_day)
                    else:
                        day_index = day_list.index(day)
                        day_count = 1
                        while day_count <= num_day: 
                            if day_index == 6:
                                day_index = 6*0
                            else:
                                day_index = day_index + 1
                            day_count += 1
                        current_day = day_list[day_index]
                        new_time = hour+':'+minute_tens+minute_units+' '+meridean+','+' '+current_day+' '+day_later.format(num_day)
            
            elif even_odd_check == 0 and meridean == 'AM':
                meridean = 'AM'
                minute = str(whole_min)
                hour = str(whole_hour - (round(12*num_meridean_change)))
                if int(minute) >= 60:
                    hour = str(int(hour) + int(minute)//60)
                if hour == '0':
                    hour = str(12)
                if int(minute) >= 60:
                    minute = str(int(minute)%60)
                num_day = round(whole_hour/24 + 1)

                minute_tens =str(int(minute)//10)
                minute_units = str(int(minute)%10)
                if day == '':
                    new_time = hour+':'+minute_tens+minute_units+' '+meridean+' '+day_later.format(num_day)
                else:
                    day_index = day_list.index(day)
                    day_count = 1
                    while day_count <= num_day:
                        if day_index == 6:
                            day_index = 6*0
                        else:
                            day_index = day_index + 1
                        day_count = day_count + 1
                    current_day = day_list[day_index]
                    new_time = hour+':'+minute_tens+minute_units+' '+meridean+','+' '+current_day+' '+day_later.format(num_day)

            if even_odd_check != 0 and meridean == 'PM':
                meridean = 'AM'
                minute = str(whole_min)
                hour = str(whole_hour - (round(12*num_meridean_change)))
                if int(minute) >= 60:
                    hour = str(int(hour) + int(minute)//60)
                if hour == '0':
                    hour = str(12)
                if int(minute) >= 60:
                    minute = str(int(minute)%60)
                num_day = round(whole_hour//24 + 1)
              
                minute_tens =str(int(minute)//10)
                minute_units = str(int(minute)%10)
                if num_day == 1:
                    if day == '':
                        new_time = hour+':'+minute_tens+minute_units+' '+meridean+' '+next_day
                    else:
                        day_index = day_list.index(day)
                        day_count = 1
                        while day_count <= num_day: 
                            if day_index == 6:
                                day_index = 6*0
                            else:
                                day_index = day_index + 1
                            day_count += 1
                        current_day = day_list[day_index]
                        new_time = hour+':'+minute_tens+minute_units+' '+meridean+', '+current_day+' '+next_day
                else:
                    if day == '':
                        new_time = hour+':'+minute_tens+minute_units+' '+meridean+' '+day_later.format(num_day)
                    else:
                        day_index = day_list.index(day)
                        day_count = 1
                        while day_count <= num_day: 
                            if day_index == 6:
                                day_index = 6*0
                            else:
                                day_index = day_index + 1
                            day_count += 1
                        current_day = day_list[day_index]
                        new_time = hour+':'+minute_tens+minute_units+' '+meridean+','+' '+current_day+' '+day_later.format(num_day)
            
            elif even_odd_check != 0 and meridean == 'AM':
                meridean = 'PM'
                minute = str(whole_min)
                hour = str(whole_hour - (round(12*num_meridean_change)))
                if int(minute) >= 60:
                    hour = str(int(hour) + int(minute)//60)
                if hour == '0':
                    hour = str(12)
                if int(minute) >= 60:
                    minute = str(int(minute)%60)
                num_day = round(whole_hour//24 + 1)
              
                minute_tens =str(int(minute)//10)
                minute_units = str(int(minute)%10)

                if num_day == 1:
                    if day == '':
                        new_time = hour+':'+minute_tens+minute_units+' '+meridean+' '+next_day
                    else:
                        day_index = day_list.index(day)
                        day_count = 1
                        while day_count <= num_day: 
                            if day_index == 6:
                                day_index = 6*0
                            else:
                                day_index = day_index + 1
                            day_count += 1
                        current_day = day_list[day_index]
                        new_time = hour+':'+minute_tens+minute_units+' '+meridean+' '+current_day+' '+next_day
                else:
                    if day == '':
                        new_time = hour+':'+minute_tens+minute_units+' '+x+' '+day_later.format(num_day)
                    else:
                        day_index = day_list.index(day)
                        day_count = 1
                        while day_count <= num_day:
                            if day_index == 6:
                                day_index = 6*0
                            else:
                                day_index = day_index + 1
                            day_count += 1
                        current_day = day_list[day_index]
                        new_time = hour+':'+minute_tens+minute_units+' '+x+','+' '+current_day+' '+day_later.format(num_day)





    return new_time
