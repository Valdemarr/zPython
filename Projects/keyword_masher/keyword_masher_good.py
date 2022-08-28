from itertools import permutations
from pathlib import Path
import os

input_words = list() # This will be populated from input.txt

# Doing some stuff so that it diddles files from the same directory where this file is
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

# Reading file in directory
f = open(os.path.join(__location__, 'input.txt'), "r") # Open and read input file

for latoo in f:
    input_words.append(latoo.strip("\n")) # This will populate the empty list with the input words from the file, while stripping away the line break
    
f.close()

print("Words given:", input_words)

# Writing result to file in directory
f2 = open(os.path.join(__location__, 'output.txt'), "w") #open and write to output file

f2.write(f"Words given: {input_words}\n\n") # Serves as a title

for i in list(permutations(input_words, 2)): #Creates the possible permutations in a list, with and output of 3 words
    string_result = " ".join(i) # Converts list to single string
    f2.write(f"{string_result}\n") #Write to output file

    print(string_result)
f2.close()




