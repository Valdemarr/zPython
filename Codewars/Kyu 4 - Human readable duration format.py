###Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds, in a human-friendly way.

#The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.

#It is much easier to understand with an example:

#* For seconds = 62, your function should return 
#    "1 minute and 2 seconds"
#* For seconds = 3662, your function should return
#    "1 hour, 1 minute and 2 seconds"
#For the purpose of this Kata, a year is 365 days and a day is 24 hours.

#Note that spaces are important.

##Detailed rules
#The resulting expression is made of components like 4 seconds, 1 year, etc. In general, a positive integer and one of the valid units of time, separated by a space. The unit of time is used in plural if the integer is greater than 1.

#The components are separated by a comma and a space (", "). Except the last component, which is separated by " and ", just like it would be written in English.

#A more significant units of time will occur before than a least significant one. Therefore, 1 second and 1 year is not correct, but 1 year and 1 second is.

#Different components have different unit of times. So there is not repeated units like in 5 seconds and 1 second.

#A component will not appear at all if its value happens to be zero. Hence, 1 minute and 0 seconds is not valid, but it should be just 1 minute.

#A unit of time must be used "as much as possible". It means that the function should not return 61 seconds, but 1 minute and 1 second instead. Formally, the duration specified by of a component must not be greater than any valid more significant unit of time.

def format_duration(seconds):
    
    year_count = 0
    seconds_in_year = 31536000
    
    day_count = 0
    seconds_in_day = 86400
    
    hour_count = 0
    seconds_in_hour = 3600
    
    minute_count = 0
    seconds_in_minute = 60
    
    if seconds == 0:
        return "now"
    
    while seconds - seconds_in_year + 1 > 0:
        year_count += 1
        seconds = seconds - seconds_in_year
        
    while seconds - seconds_in_day + 1 > 0:
        day_count += 1
        seconds = seconds - seconds_in_day
    
    
    while seconds - seconds_in_hour + 1 > 0:
        hour_count += 1
        seconds = seconds - seconds_in_hour
    
    
    while seconds - seconds_in_minute + 1 > 0:
        minute_count += 1
        seconds = seconds - seconds_in_minute
    
    time_list = [year_count, day_count, hour_count, minute_count, seconds]





    #years
    if year_count == 1:
        year_result = str(year_count) + " year, "
    elif year_count > 1:
        year_result = str(year_count) + " years, "
    else: 
        year_result = ""
    
    #days
    if day_count == 1:
        day_result = str(day_count) + " day, "
    elif year_count > 1:
        day_result = str(day_count) + " days, "
    else: 
        day_result = ""
        
    #hours
    if hour_count == 1:
        hour_result = str(hour_count) + " hour, "
    elif hour_count > 1:
        hour_result = str(hour_count) + " hours, "
    else: 
        hour_result = None
        
    
    #minutes
    if minute_count == 1:
        minute_result = str(minute_count) + " minute, "
    elif minute_count > 1:
        minute_result = str(minute_count) + " minutes, "
    else: 
        minute_result = ""
    
    #seconds
    if seconds == 1:
        second_result = str(seconds) + " second"
    elif seconds > 1:
        second_result = str(seconds) + " seconds"
    else: 
        second_result = ""
    #final
    #return f"{year_result}{day_result}{hour_result}{minute_result}{second_result}"

    
    
    time_list_result = [year_result, day_result, hour_result, minute_result, second_result]
    
    new_list = []
    
    for element in time_list:
        if element != 0:
            new_list.append(element)
            
    print("new list: ", new_list)
    
    print(time_list)
    
    print("time list result: ",time_list_result)
    
    if len(new_list) == 2:
        print("and".join(new_list))