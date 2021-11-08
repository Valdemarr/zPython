def alphabet_war(fight):
    points_left = 0
    points_right = 0

    left_l = ["w", "p", "b", "s"]
    left_p = [4, 3, 2, 1]

    right_l = ["m", "q", "d", "z"]
    right_p = [4, 3, 2, 1]

    for i in fight:
        if i in left_l:
            # find index of every letter in variable fight in either left_l or right_l
            x = left_l.index(i)
            # use that index to get and store the point corresponding to that letter, from either left_p or right_p
            y = left_p[x]
            # accumulate points
            points_left += int(y)

        if i in right_l:
            # same as above
            x = right_l.index(i)

            y = right_p[right_l.index(i)]

            points_right += int(y)

    if points_left == points_right:
        return "Let's fight again!"
    elif points_left > points_right:
        return "Left side wins!"
    elif points_left < points_right:
        return "Right side wins!"


def test(b):
    print(f"Test print: {alphabet_war(b)}")


test("wwww mmmmm")
