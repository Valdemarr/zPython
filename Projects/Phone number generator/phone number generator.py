import random


def gen_phone_num(n):
    phone_number = ""

    for i in range(n):
        phone_number += str(random.randint(0, 9))
    print("phone numbeR: " + str(phone_number))

    # WRITE phone number HISTORY
    f = open(r"G:\Mit drev\Rayndom\zPython\Projects\Phone number generator\phone numbers.txt", "a")
    f.write(str(f"{phone_number}\n"))
    f.close()

# HOW MANY TO MAKE?


def amount_of_pn(n):
    for i in range(n):
        gen_phone_num(8)


amount_of_pn(50)
