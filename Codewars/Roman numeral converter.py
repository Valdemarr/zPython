def solution(roman):
    result = 0

    numerals = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000}

    for letter in roman:
        result += numerals[letter-1]

    return result
