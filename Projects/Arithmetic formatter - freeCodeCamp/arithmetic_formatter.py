#FCC python exam 1
import re

def arithmetic_arranger(problems, calculate=False):
    fn = []
    op = []
    sn = []
    dash = []
    actual_calctual = []

    arranged_problems = ""

    for i in problems:
        split = re.split("\s", i)
        fn.append(split[0])
        op.append(split[1]+ " ")
        sn.append(split[2])

    amount = len(fn)


    for slice in range(amount):
        #--RAISING ERRORS--#
        if fn[slice].isdigit() == False or sn[slice].isdigit() == False:
            raise Exception("Error: Numbers must only contain digits.")
        else:
            pass

        if len(fn[slice]) > 4 or len(sn[slice]) > 4:
            raise Exception("Error: Numbers cannot be more than four digits.")
        else:
            pass

        if "+" in op[slice]:
            actual_calctual.append(int(fn[slice]) + int(sn[slice]))
        elif "-" in op[slice]:
            actual_calctual.append(int(fn[slice]) - int(sn[slice]))
        else:
            raise Exception("Error: Operator must be '+' or '-'.")

        #--FIND LENGTH DIFFS--#
        if len(fn[slice]) > len(sn[slice]):
            diff = len(fn[slice]) - len(sn[slice])
            sn[slice] = " "*diff + sn[slice]
            
        else:
            diff = len(sn[slice]) - len(fn[slice])
            fn[slice] = " "*diff + fn[slice]
            
        
        fn[slice] = "  " + fn[slice] #Adds a 2 spaces before fn, as there are always at least 2 spaces before
        sn[slice] = str(op[slice]) + sn[slice] #Makes sn contain both the operator, space between and the number

        sn_calc_diff = len(sn[slice]) - len(str(actual_calctual[slice])) #Get the difference between sn (which is the same length as the dashes), in a string because it's an int
        actual_calctual[slice] = " " * sn_calc_diff + str(actual_calctual[slice]) #Add the difference in spaces before the result

    #--PRINTING THE STUFF--# ooorr.. ASSEMBLING THE STUFF
    holder = ""

    for number in fn:
        holder += number + "    "
    
    arranged_problems += holder + "\n"
    #print(holder)
    holder = ""

    for numbi in sn:
        holder += numbi + "    "
    
    #print(holder)
    arranged_problems += holder + "\n"
    holder = ""


    for dash in range(amount):
        holder += len(sn[dash]) * "-" + "    "

    arranged_problems += holder + "\n"
    #print(holder)
    holder = ""

    #--OPTIONAL OUTPUT--#
    if calculate == True:
        for result in actual_calctual:
            holder += str(result) + "    "
        #print(holder)
        arranged_problems += holder

    return arranged_problems

print(arithmetic_arranger(["3801 - 2", "123 + 49"], True))

#there are unnecessary 4 spaces on each line