def order(sentence):
    ranges = range(1, 100)
    for character in sentence:
        if character in ranges:
            print(character)
