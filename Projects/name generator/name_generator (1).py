import random as ran
from pandas import *

# Importing data from Excel spreadsheet
excelsheet = pandas.read_excel(
    r"G:\Mit drev\Rayndom\zPython\Projects\name generator\Spreadsheet_with_words.xlsx")

adjectives = excelsheet['Adjectives'].tolist()
nouns = excelsheet['Nouns'].tolist()

# Counting number of words in spreadsheet
len_adj = len(adjectives)
len_nou = len(nouns)

# Intro with calculation of unique combinations
print("Welcome to the username generator. There are exactly " +
      str(len_adj*len_adj*len_nou) + " unique combinations")

# Picking ran adjectives, nouns and numbers(from 1-100)
r_adj_x2 = ran.sample(adjectives, 2)
r_nou = ran.choice(nouns)
r_num = ran.choice(range(10, 101))

# Option of adding number to username
use_numbers = False
if use_numbers is False:
    print(f" Your name is: {r_adj_x2[0]}{r_adj_x2[1]}{r_nou}")
else:
    print("Do you want numbers in your name? Type Y / N:")
    reply = input()
    # Output
    if reply == "Y" or reply == "y":
        print(f" Your name is: {r_adj_x2[0]}{r_adj_x2[1]}{r_nou}{r_num}")
    elif reply == "N" or reply == "n":
        print(f" Your name is: {r_adj_x2[0]}{r_adj_x2[1]}{r_nou}")
    else:
        print(
            f"You should really learn to read instructions... But here's your username without numbers: {r_adj_x2[0]}{r_adj_x2[1]}{r_nou}")


# Users can cumulatively add new words and expand the database
# Filters to avoid slurs and racism in place
# Generate name based on user input
# Randomly choose x2 adj + nou / verb + adj + nou
# Remove already generated names
# Count how many names there can be with numbers
# Make interface
