# simpliefied morse_code

list = ["V", "v", "A", "a", "L", "l"]
lc = ["v", "a", "l"]
uc = ["V", "A", "L"]


def morse(text):
    text2list = []
    index_list = []
    conv_index_list = []
    for letter in text:
        #index_num = index(text)
        text2list.append(letter)

    for element in text2list:
        what_index = list.index(element)
        index_list.append(what_index)

    for beep in index_list:
        conv_index_list.append(beep-1)

    print(text2list)
    print(f"whatindex: {what_index} and type {type(what_index)}")
    print(index_list)
    print(conv_index_list)


test = "lav"

morse(test)
