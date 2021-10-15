from itertools import product
from string import ascii_uppercase


def pw_c(word):
    for combo in product(ascii_uppercase, repeat=len(word)):
        print("".join(combo) + f"elapsed time: {tim}")


pw_c("lolo")

bigtest = 23214
