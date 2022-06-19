import random
import os

def gen_phone_num(n):
    phone_number = ""
    

    for i in range(n):
        phone_number += str(random.randint(0, 9))
    print(f"Generating number: {phone_number}", end="\r")
    print("")

    # WRITE phone number HISTORY
    f = open("G:\Mit drev\Rayndom\zPython\Projects\Phone number generator\phone numbers.txt", "a")
    f.write(str(f"\n{phone_number}"))
    f.close()

    
# HOW MANY TO MAKE?

def amount_of_pn(num):
    #count = 0

    for i in range(num):
        gen_phone_num(8)
        #count += 1
        #print(f"Generating: {count}/{num} // ")
    
    f = open(r"G:\Mit drev\Rayndom\zPython\Projects\Phone number generator\phone numbers.txt", "r")
    line_count = 0
    for line in f:
        if line != "\n":
            line_count += 1
    f.close()

    size = os.path.getsize(r"G:\Mit drev\Rayndom\zPython\Projects\Phone number generator\phone numbers.txt")

    size = round(size / 1000)

    print("You added", num, "more lines.")
    print("There are now a total of ", line_count, " lines.")
    print('\033[96m' + "File size:", size, "KB")

amount_of_pn(100)