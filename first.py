# Calculation
import numpy as np
print(5 / 8)
# with power
print(4 ** 2)

# ?Declaration? of variables
valdemar_age = 24
valdemar_personality = "nice"
# with calculations
one_year_older = valdemar_age+1
print(one_year_older)

double_personality = valdemar_personality+valdemar_personality
print(double_personality)

# Data types                                                                 example_variable=
# int (integer): whole number without fractional part -                      1
# float: number with an integer and a fractional                             part, - 1.1
# str (string): represents text. Done with "" -                              "hello world"
# bool (boolean): represents logical values, can only be True or False -     True
# Lists: Used to store and call several ?things? by using []                 [item1, item2, item3]

# Find out the type of a variable
print(type(one_year_older))

# Type conversion - You can not just paste together 2 strings, they have to be the same or converted
print("Valdemar is "+str(valdemar_age) + " years old and he is " + valdemar_personality)
# You can also convert eg. a string to a float
floaty_string = "100"
floaty_float = float(floaty_string)

# Lists-Lists-Lists-Lists-
weight_sep = 90.1
weight_oct = 89.3
weight_nov = 87.7
weight_dec = 90.2

weight_progress = [weight_sep, weight_oct, weight_nov, weight_dec]
print(weight_progress)
# Using strings along with varibles that contain floats
weight_progress_labels = ["September", weight_sep, "October",
                          weight_oct, "November", weight_nov, "December", weight_dec]
print(weight_progress_labels)
# And you can make lists within lists, since lists are a data type too
list_within_list = [["September", weight_sep], ["October", weight_oct],
                    ["November", weight_nov], ["December", weight_dec]]
print(list_within_list)
# 0-indexing and subsetting - You can grab a specific element starting at 0
print(list_within_list[1])  # and get the weight of October
print(list_within_list[-3])  # using a negative index returns the same as [1]
# Slicing: You can also create variables or just print the range of a list.
# The start of the range is included, while the end is not NB
print(list_within_list[2:5])
# You can also specify if the list should start from the beginning with :
print(list_within_list[:5])
# You can also calculate with list elements
autumn_weight = list_within_list[0]+list_within_list[1]+list_within_list[2]
print(autumn_weight)

# List manipulation
# Changing
weight_progress[0] = 89.9
list_within_list[3] = ["DECUMBRE", 900.2]

print(list_within_list)
# Adding and removing items
weight_progress_labels_addition = weight_progress_labels + \
    ["Januar", 88.8]  # in another list. fuckoff
del(weight_progress_labels_addition[0])  # deletion
print(weight_progress_labels_addition)

# NB About Changing
wp1 = weight_progress  # making a new variable == old variable
wp1[1] = 85.0  # changing the new variable
print(wp1)
# also changes the old variable's outcome. Because they are both referencing the SAME list in the memory
print(weight_progress)
# by using the list: function or slicing it, you create a new list that doesn't affect the one_year_olde
wp = list(weight_progress)
wp = weight_progress[:]
print(wp)

# FUNCTIONSS WOOOHOO LETS GO
# print() see result of code
# type() figure out the type of a variable
# str() converts another data type to a string
# int() converts another data type to a integer
# bool() converts another data  type to a boolean
# float() converts another data type to a float
# len() get the length of a variable
# help() get help on how to use a function - help(len)
# complex() i have no idea
# sorted()
# round()

# max() takes the highest value of a list
heaviest = max(wp)
print(heaviest)
# round() rounds the specified number to the specified rounding precision(ndigits). If left out, rounds to nearest integer
print(round(wp[0]))
# Store output of a function as a new variable
wp_type = type(wp)
print(type(wp))

print(len(wp))

# sorted list
print(sorted(wp))  # simple autofill, ascending
# specified iterable and whether reverse or not, in this case, descending order
print(sorted(wp, reverse=True))

# Methods
# .index()
# .count(input goes here) like vp.count(e) = 1
# .capitalize()
# .replace()
# .upper() - uppercase
# .remove()
# .reverse()
# .append()

wpl = weight_progress_labels
print(wpl.index("September"))  # prints as 0...
wp.count(87.7)  # counts how many times the number occurs in the list
# str Methods
vp = valdemar_personality
vp.capitalize()  # capitalizes letter
vp.replace("ic", "aiv")  # replaces letters
# EVERYTHING is an object. Each object has specified methods associated. Depending on the object type, the availabe methods are different.
vp_up = vp.upper()

# Print out place and place_up
print(vp)
print(vp_up)

# Packages
# A directory of Python scripts. Each script is a module. They specify functions, methods and new Python types. Available online.

# numpy
# math

# Numpy is a good package for arrays, ex
# to import the whole numpy package:
# import numpy
# To refer to the array function of the numpy package - Only a part of it:
# numpy.array([1,2,3]) OR from numpy import array
# you can also import it as a specified custom name to not have to write as much:
# import numpy as np - and it would become np.array([1,2,3]) instead

# you want to use the function inv(), which is in the linalg subpackage of the scipy package. You want to be able to use this function as follows:
# To be able to do this: my_inv([[1,2], [3,4]])
# You must import like this: from scipy.linalg import inv as my_inv

# Numpy
# import numpy as np
# To calculate BMI's
height = [1.73, 1.68, 1.71, 1.89, 1.79]
weight = [65.4, 59.2, 63.6, 88.4, 68.7]

# weight/height**2 DOESN'T work because Python can't calculate with lists
# So we convert them to numpy arrays
height_np = np.array(height)
weight_np = np.array(weight)
print(weight_np/height_np**2)  # which just works because numpy works element-wise
# NB Numpy assumes that a list/array only contain 1 type of data, so [1.0, "Yes", True] will all become floats

# Numpy subsettings
bmi = weight_np/height_np**2
print(bmi[0])  # grab get of an array as with regular python list
print(bmi > 23)  # this outputs true/false statements if they are above/under 23
print(bmi[bmi > 23])  # Using this grabs the actual values of BMI's over 23

# 2D Numpy arrays
# Basically excel-sheet?

# TIPS AND TRICKS


def is_good(a):
    # easy way to write if statements
    return {a == 1: "a=1",
            a > 1: "a is more than 1",
            a < 1: "a is less than 1"
            }[True]


print(is_good(2))
