
# VARIABLES
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
           "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

lstring = "abcdefghijklmnopqrstuwvxyz"


def crack_pw(password):
    result1 = ""
    result2 = ""
    result3 = ""
    result4 = ""
    result5 = ""
    result6 = ""
    result7 = ""
    result8 = ""
    result9 = ""
    result10 = ""

    true_result = ""
    while password != result1:

        # 1 LETTER
        for i1 in lstring:
            result1 = i1
            # CHECKING PASSWORD
            if result1 == password:
                print(f"Found password: {result1}")
                return result1

        # 2 LETTERS
        for i1 in lstring:
            result = i1
            for i2 in lstring:
                result2 = result + i2
                # CHECKING PASSWORD
                if result2 == password:
                    print(f"Found password: {result2}")
                    return result2
        break
    print("No matching password found")
    #result += pw
    # print(result)


crack_pw("ji")
