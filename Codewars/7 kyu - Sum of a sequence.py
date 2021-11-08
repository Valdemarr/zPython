def sequence_sum(begin_number, end_number, step):
    # your code here
    x = begin_number
    result = begin_number
    if begin_number > end_number:
        return 0
    elif end_number % step != 0:
        return "oh no"
        result = 5
    else:
        while x < end_number or x != end_number:
            x += step
            result += x
            print(f"loop: {x}")
        return result


def test():
    b = 1
    e = 5
    s = 3
    print(f"result: {sequence_sum(b, e, s)}")


test()
