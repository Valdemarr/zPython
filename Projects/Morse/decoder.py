list = ["A", ".-",     "B", "-...",   "C", "-.-.",
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
        "9", "----.", " ", ""]


def morse(text):
    index_list = []
    conv_index_list = []
    result = ""

    text2list = text.replace("   ", "  ").split(" ")
    print(text)
    print(text2list)

#    for letter in text:
    # Put the letters into a list --> ["v", "a", "l"]
#        text2list.append(letter)

    for element in text2list:
        # Find the index of each element from the list "text2list" in the list "list"
        what_index = list.index(element)
        # Put indices into list --> [1, 3, 5]
        index_list.append(what_index)

    for element2 in index_list:
        # remove -1 from each index element in the list "index_list" into new list "conv_index_list"
        conv_index_list.append(element2-1)

    for loop in conv_index_list:
        # Convert new index numbers back to letters
        result += list[loop]

    print(f"result: {result}")


test = ".... . -.--   .--- ..- -.. ."

morse(test)
