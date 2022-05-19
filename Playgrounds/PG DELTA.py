import time
x = 1
while True:
    for i in range(11):
        x += 1
        print('\033[96m' + "U25A1.gif"*x)  # end="\r"
        time.sleep(0.01)

    for i2 in range(10):
        x -= 1
        print('\033[91m' + "⬛"*x)
        time.sleep(0.01)


print(x)
