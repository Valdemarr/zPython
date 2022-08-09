import os

# Doing some stuff so that it diddles files from the same directory where this file is
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

# Reading file in directory
f = open(os.path.join(__location__, 'input.txt'), "r") # Open and read input file
#needs reading line here
f.close()

# Writing result to file in directory
f2 = open(os.path.join(__location__, 'output.txt'), "w") #open and write to output file
f2.write("whatever") #Write to output file
f2.close()