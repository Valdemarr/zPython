#all possible number plates generator
import string

letter_list = list(string.ascii_uppercase)

for letter_1 in letter_list:
    for letter_2 in letter_list:
        for digit_1 in range(10):
            for digit_2 in range(10):
                for digit_3 in range(10):
                    for digit_4 in range(10):
                        for digit_5 in range(10):
                            print(letter_1 + letter_2 + " " +str(digit_1) + str(digit_2) + " " +str(digit_3) + str(digit_4) + str(digit_5))
                            