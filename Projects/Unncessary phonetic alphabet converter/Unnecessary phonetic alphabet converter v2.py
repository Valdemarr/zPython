def unphalcon(text_to_convert: str, latinize:bool, print_it:bool):
    text_to_convert = text_to_convert.upper() # Make all characters uppercase so they're easier to work with
    alphacon = ""
    latinized = ""

    alphabet = {"A": "Alpha",       "B": "Bravo",       "C": "Charlie",
                "D": "Delta",       "E": "Echo",        "F": "Foxtrot",
                "G": "Golf",        "H": "Hotel",       "I": "India",
                "J": "Juliett",     "K": "Kilo",        "L": "Lima",
                "M": "Mike",        "N": "November",    "O": "Oscar",
                "P": "Papa",        "Q": "Quebec",      "R": "Romeo",
                "S": "Sierra",      "T": "Tango",       "U": "Uniform",
                "V": "Victor",      "W": "Whiskey",     "X": "X-ray",
                "Y": "Yankee",      "Z": "Zulu",        " ": "   "}

    for char in text_to_convert:
        if char in alphabet.keys(): # If the character is in the above alphabet list, 
            tempy = alphabet[char] # Hold the value - The phonetic word for the letter
            
            alphacon += tempy + " " # Store it in a new variable and keep adding every value every loop
            latinized += tempy[0:2] # Store only the first 2 characters and keep adding every loop

        elif char not in alphabet.keys(): # If the character is not in the alphabet list,
            alphacon += char + " " # Just let it through

    spacer = len(text_to_convert) //2 * 2 # Find the middle of the string
    first_half = latinized[:spacer].lower().capitalize() # Split up at the middle, and make the first half lower cased, then firt letter uppercase
    second_half = latinized[spacer:].lower().capitalize() # Same as above

    latinized = first_half + " " + second_half # Redeclaring the old variable with the new content so we get a space in the middle

    if latinize == False: # If latinize is False, 
        result = alphacon # the result is the regular unphalcon
    else: # Else
        result = latinized # result is the latinized

    if print_it == True: # If print_it is True,
        print(f"{text_to_convert} -> {result}") # print result
    else: # Else
        return result # return result

unphalcon("Janus", True, True)
