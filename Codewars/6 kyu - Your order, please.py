# Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.

# Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

# If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.

# Examples
# "is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
# "4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"

def order(sentence):
    word_list = sentence.split()  # Put the words into a list
    number_list = list()  # Make new list for numbers
    result = ""

    for character in sentence:  # Go through every character in the original sentence
        if character.isdigit():  # If it detects a number,
            number_list.append(character)  # It will add them to our empty list

    try:  # We're setting up a try/except because the empty test strings in sentence will bring up an error
        # With this line i found on StackOverflow, both our numbers_list AND word_list are sorted after the number_list values
        number_list, word_list = zip(*sorted(zip(number_list, word_list)))

        for word in word_list:  # Go through every word in the newly sorted word_list
            result += word + " "  # And add them to empty result string, with an added space

    except:  # When empty strings come up
        pass  # Nothing happens, it just moves on

    # Because the for loop above adds an unnecessary space at the end of the string, strip() removes it again
    result = result.rstrip()

    return result


print(order("about7 did4 me8 fuc3k Wh1at you5 th2e say6"))
