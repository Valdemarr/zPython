import random
import os

# Doing some stuff so that it diddles files from the same directory where this file is
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


def gen_phone_num(n):
    phone_number = ""
    

    for i in range(n):
        phone_number += str(random.randint(0, 9))
    print(f"Generating number: {phone_number}", end="\r")
    print("")

   
    
    # Writing result to file in directory - GOOD FOR LOGGING
    f = open(os.path.join(__location__, 'phone numbers.txt'), "a") #open and write to output file
    f.write(str(f"\n{phone_number}")) #Write to output file
    f.close()

    
# HOW MANY TO MAKE?

def amount_of_pn(num):
    #count = 0

    size = os.path.getsize(os.path.join(__location__))

    for i in range(num):
        gen_phone_num(8)
        #count += 1
        #print(f"Generating: {count}/{num} // ")
    
    f = open(os.path.join(__location__, 'phone numbers.txt'), "r") #open and write to output file
    line_count = 0
    for line in f:
        if line != "\n":
            line_count += 1
    f.close()



    size = round(size / 1000)

    print("You added", num, "more lines.")
    print("There are now a total of ", line_count, " lines.")
    print('\033[96m' + "File size:", size, "KB")

amount_of_pn(100)