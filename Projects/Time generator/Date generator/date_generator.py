from calendar import month
import random

def date_generator(start_year:int, end_year:int, separator:str, amount:int, uniformity:bool, day_month_switch:bool):
    sorted_list = []

    for i in range(amount):
        month = random.randint(1, 12) #Select random number between 1-12, representing a month

        day_max = 0

        if month == 2: #If the month is February
            day_max = 28 #The max days of the month is 28
        elif month == 4 or month == 6 or month == 9 or month == 11: #If the month is April, June, September or November
            day_max = 30 #The max days of the month is 30
        else: #If month January, March, May, July, August or December
            day_max = 31 #Max days 31

        year = str(random.randint(start_year, end_year)) #Find random year between start_year and end_year. And string it

        month = str(month) #String the month now that we don't need it as an integer anymore (tbh we never realler NEEDED it to be an int)
        
        day = str(random.randint(1, day_max)) #Pick a day between 1 and the max days we have found, depending on which month it is. And string it

        if uniformity == True and len(month) == 1: #If the uniformity parameter is True and the month consists of a single digit
            month = "0" + month #Add 0 in front of it
        
        if uniformity == True and len(day) == 1: #If the uniformity parameter is True and the day consists of a single digit
            day = "0" + day #Add 0 in front of it

        date_normal = day + separator + month + separator + year
        date_switched = month + separator + day + separator + year
        
        final_date = ""

        if day_month_switch != True:
            final_date = date_normal
        else:
            final_date = date_switched
    
        sorted_list.append(final_date)

    def last_4_sort(input):
        return input[-4:]

    sorted_list.sort(key=last_4_sort)

    if amount > 1:
        print(sorted_list)
    else:
        print(final_date)

date_generator(2016, 2022, "/", 5, True, False)
