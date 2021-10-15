def reverse_words(text):
    if "  " in text:
        text = text[::-1]
        text = text.split()
        text = text[::-1]
        text = "  ".join(text)
        return text
    else:
        text = text[::-1]
        text = text.split()
        text = text[::-1]
        text = " ".join(text)
        return text


print(reverse_words("This is a string"))
