def un_phon_al_conv(text: str):
    text = text.upper()
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

    for i in text:
        if i in alphabet.keys():
            result += alphabet[i]
            result += " "
        if i not in alphabet.keys():
            result += i
            result += " "

    un = open(
        r"G:\Mit drev\Rayndom\zPython\Projects\Unncessary phonetic alphabet converter\unphalconed.txt", "a")
    un.write(f"New unphalcone: \n{result}\n\n")
    un.close()

    print(f"'{j}' sucessfully written to unphalconed.txt")


f = open(r"G:\Mit drev\Rayndom\zPython\Projects\Unncessary phonetic alphabet converter\file.txt", "r")
j = f.read()
f.close()


print(un_phon_al_conv(j))
