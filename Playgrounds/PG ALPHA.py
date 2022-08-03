from mpmath import mp
import re

mp.dps = 100 #No. of digits to display (-1)
our_pi = mp.pi

def count_digits(big_number):
    #emp_list = list()
    emp_string = ""

    big_number = str(our_pi)
    big_number = re.findall("\.(\S+)", big_number) #Only return digits after the point
   
    for i in big_number:
        emp_string += i
    

    counting = dict()
    for digit in emp_string: #For every digit in our huge number
        if digit not in counting: #If the digit does not already exist in our counting dictionary
            counting[digit] = 1 #Add the digit as a key and a start value of 1
        else:
            counting[digit] = counting[digit] +1 #However, if the digit key does exist in the counting dictionary, increase it by +1
    
    result = {key: val for key, val in sorted(counting.items(), key = lambda ele: ele[0])} #Sorting the dictionary by keys
    
    print(big_number)
    print(str(result))
    
    print("0:",list(result.values())[0]*"█", list(result.values())[0])
    print("1:",list(result.values())[1]*"█", list(result.values())[1])
    print("2:",list(result.values())[2]*"█", list(result.values())[2])
    print("3:",list(result.values())[3]*"█", list(result.values())[3])
    print("4:",list(result.values())[4]*"█", list(result.values())[4])
    print("5:",list(result.values())[5]*"█", list(result.values())[5])
    print("6:",list(result.values())[6]*"█", list(result.values())[6])
    print("7:",list(result.values())[7]*"█", list(result.values())[7])
    print("8:",list(result.values())[8]*"█", list(result.values())[8])
    print("9:",list(result.values())[9]*"█", list(result.values())[9])

    """
    for i in big_number:
        newly.append(i)

    newly.sort()

    marky = "".join(newly)
    
    return marky
    """
print(count_digits(our_pi))