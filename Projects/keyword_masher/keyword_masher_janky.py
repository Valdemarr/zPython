import random
import math

# Calculate how many possible permutations the input has
amount_of_words = 4
words_in_outcome = 3

max_permutations = math.factorial(amount_of_words) / math.factorial((amount_of_words-words_in_outcome)) #thanks to https://www.calculator.net/permutation-and-combination-calculator.html?cnv=4&crv=3&x=96&y=16

def keyword_masher(a,b,c,d):
    list_of_given_keywords = [a, b, c, d]

    full_list = list()

    holder = ""

    count = 0

    while len(full_list) < max_permutations:
        result = ""
        holder = random.choices(list_of_given_keywords, k=3)
        holder = set(holder)
        
        if len(holder) < words_in_outcome:
            continue

        else:
            for loop in holder:
                result += loop + " "

            if result not in full_list:
                full_list.append(result.strip())
                count += 1
                print("New permutation:", count)
                
            
            else:
                count += 1
                print("Old permutation", count)
                continue
        
    return full_list

print(keyword_masher("X", "I", "V", "M"))    

