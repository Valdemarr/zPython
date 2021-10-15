import random

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


def gen_phone_num(n):
    phone_number = ""

    for i in range(n):
        phone_number += str(random.randint(0, 9))
    print("phone numbeR: " + str(phone_number))

    # WRITE phone number HISTORY
    f = open(r"G:\Mit drev\Rayndom\zPython\Projects\Phone number generator\phone numbers.txt", "a")
    f.write(str(f"{phone_number}\n"))
    f.close()


def amount_of_pn(n):
    for i in range(n):
        gen_phone_num(8)


amount_of_pn(500)
