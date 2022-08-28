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

    #--CALCULATION--#
    for j in range(amount): #Determine (from the input operator) wether or not it should add or subtract
        if "+" in op[j]:
            actual_calctual.append(int(fn[j]) + int(sn[j]))
        elif "-" in op[j]:
            actual_calctual.append(int(fn[j]) - int(sn[j]))
        else:
            raise Exception("Error: Operator must be '+' or '-'.")

    
    

    for slice in range(amount):
        
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

    #--PRINTING THE STUFF--#
    holder = ""

    for number in fn:
        holder += number + "    "
    
    print(holder)
    holder = ""

    for numbi in sn:
        holder += numbi + "    "
    
    print(holder)
    holder = ""

    #hold_holder = []

    for dash in range(amount):
        holder += len(sn[dash]) * "-" + "    "
        #hold_holder.append(holder)

    #print(hold_holder)

    print(holder)
    holder = ""

    #--OPTIONAL OUTPUT--#
    if calculate == True:
        for result in actual_calctual:
            holder += str(result) + "    "
        print(holder)

    return arranged_problems

print(arithmetic_arranger(["0 + 8", "1 - 3801", "929 + 9999", "3 - 49"], True))