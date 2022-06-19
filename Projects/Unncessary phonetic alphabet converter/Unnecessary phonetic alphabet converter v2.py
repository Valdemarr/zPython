def un_phon_al_conv(text_to_convert: str):
    text_to_convert = text_to_convert.upper()
    result = ""

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
            result += alphabet[i]
            result += " "
        if i not in alphabet.keys():
            result += i
            result += " "

    fhand = open(
        r"G:\Mit drev\zPython\Projects\Unncessary phonetic alphabet converter\unphalconed.txt", "a")
    fhand.write(f"New unphalcone: \n{result}\n\n")
    fhand.close()

    print(f"'{text_to_convert}' sucessfully written to unphalconed.txt")
    return result

print(un_phon_al_conv("valdemar"))
