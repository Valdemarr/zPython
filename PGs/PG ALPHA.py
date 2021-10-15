def decodeMorse(morse_code):
    # ToDo: Accept dots, dashes and spaces, return human-readable message
    return morse_code.replace('.', MORSE_CODE['.']).replace('-', MORSE_CODE['-']).replace(' ', '')


def morse_decoder(text):
    morse = ["A", ".-",     "B", "-...",   "C", "-.-.",
             "D", "-..",    "E", ".",      "F", "..-.",
             "G", "--.",    "H", "....",   "I", "..",
             "J", ".---",   "K", "-.-",    "L", ".-..",
             "M", "--",     "N", "-.",     "O", "---",
             "P", ".--.",   "Q", "--.-",   "R", ".-.",
             "S", "...",    "T", "-",      "U", "..-",
             "V", "...-",   "W", ".--",    "X", "-..-",
             "Y", "-.--",   "Z", "--..",

             "0", "-----",  "1", ".----",  "2", "..---",
             "3", "...--",  "4", "....-",  "5", ".....",
             "6", "-....",  "7", "--...",  "8", "---..",
             "9", "----."]

    # Making the function parameter a list
    text = text.split()

    result = ""
    list_of_indices = []

    for i in text:
        if i in morse:
            list_of_indices.append(int(morse.index(i)))

#    for i in list_of_indices:
#        print(f"2nd for: {morse[list_of_indices[i]]}")

    list_of_indices_0 = list_of_indices[0]
    decode = morse[list_of_indices_0 - 1]

    print(f"index test: {morse[list_of_indices[0]-1]}")
    print(f"decode: {decode}")

    print(f"text: {text}")
    print(f"list_of_indices: {list_of_indices}")
    print(result)


test = "--.. .--. -.-- - .... --- -."

morse_decoder(test)

test = 2
