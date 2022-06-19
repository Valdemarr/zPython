import random

def random_time(hour_start, hour_end, amount):
    
    for i in range(amount):  
        hour = str(random.randint(hour_start, hour_end-1)) #Pick a random number between the start_hour and end_hour parameter and turn it into a string

        if len(hour) == 1: #If it's only 1 digit
            hour = "0" + hour #Add an extra 0 in front of it, just to make it uniform and nice :)
        
        minute = str(random.randint(0,60)) #Pick a random number between 0 and 60

        if len(minute) == 1: #And again, if it's only 1 digit
            minute = "0" + minute #Add a 0 for uniformity
        
        time = hour + ":" + minute #Our randomly generated time in a variable

        print("Random time:", time)

        # WRITE result to .txt file
        f = open(r"G:\Mit drev\zPython\Projects\Time generator\times.txt", "a")
        f.write(str(f"\n{time}"))
        f.close()

random_time(8, 17, 20)