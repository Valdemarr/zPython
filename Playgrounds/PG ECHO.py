# simpliefied morse_code

list = ["V", "v", "A", "a", "L", "l"]
lc = ["v", "a", "l"]
uc = ["V", "A", "L"]


def morse(text):
    text2list = []
    index_list = []
    conv_index_list = []
    result = ""

    for letter in text:
        # Put the letters into a list --> ["v", "a", "l"]
        text2list.append(letter)

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

    print(result)


test = "val"

morse(test)
