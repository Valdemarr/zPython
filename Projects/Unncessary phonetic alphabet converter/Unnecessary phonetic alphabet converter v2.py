def unphalcon(text_to_convert: str, latinize:bool, print_it:bool):
    text_to_convert = text_to_convert.upper()
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

    for i in text_to_convert:
        if i in alphabet.keys():
            tempy = alphabet[i]
            
            alphacon += tempy + " "
            latinized += tempy[0:2]

        elif i not in alphabet.keys():
            alphacon += i + " "


    spacer = len(text_to_convert) //2 * 2
    first_half = latinized[:spacer].lower().capitalize()
    second_half = latinized[spacer:].lower().capitalize()

    #print(first_half + " " + second_half)
    latinized = first_half + " " + second_half


    if latinize == False:
        result = alphacon
    else:
        result = latinized

    #fhand = open(   r"G:\Mit drev\zPython\Projects\Unncessary phonetic alphabet converter\unphalconed.txt", "a")
    #fhand.write(f"New unphalcon, latinize is {latinize}: \n{result}\n\n")
    #fhand.close()

    #print(f"'{text_to_convert}' sucessfully written to unphalconed.txt")
    if print_it == True:
        print(result)
    else:
        return result

unphalcon("valdemar", True, True)
