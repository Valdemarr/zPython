# password cracker alt - recursion method


# VARIABLES
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
           "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

lstring = "abcdefghijklmnopqrstuwvxyz"

password = "g"


def crack_pw():
    result1 = ""

    # 1 LETTER
    for i1 in lstring:
        result1 = i1
        # CHECKING PASSWORD
        if result1 == password:
            print(f"Found password: {result1}")
            return result1
        crack_pw()

    print("No matching password found")
    return


crack_pw()
