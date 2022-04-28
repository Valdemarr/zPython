def order(sentence):
    word_list = sentence.split()
    number_list = list()
    result = ""

    #ranges = range(1, 100)
    for character in sentence:
        if character.isdigit():
            number_list.append(character)

    try:
        number_list, word_list = zip(*sorted(zip(number_list, word_list)))

        for word in word_list:
            result += word + " "
    except:
        pass

    result = result.rstrip()

    print(result)


order("about7 did4 me8 fuc3k Wh1at you5 th2e say6")
