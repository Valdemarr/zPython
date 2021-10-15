from tkinter import *
from tkinter import messagebox

import random

# DRAWING WINDOW
top = Tk()
top.geometry("400x400")

# VARIABLES
outcomes = range(1, 6)

display = ""
result = ""

# FUNCTION


def dice_roll():
    chosen_dice = int(SB1.get())
    roll = 0
    result = 0

    for i in range(chosen_dice):
        roll = random.choice(outcomes)
        result += roll
        print(f"Roll no. {i+1}")
        print(f"You rolled: {roll}\n")

    # command line info
    print(f"def result = {result}")

    # WRITING TO LOG FILE
    f = open("rolls_log.txt", "a")
    f.write(str(f"Rolled a: {result}\n"))
    f.close()

    display = result
    top.update()

    msg = messagebox.showinfo("Dice roller", f"You rolled: \n\n{result}")


def exit():
    top.destroy()


# TKINTER GUI SHIT
wel_lab = Label(top, text="""----------------------------------------------
*=-=-=-=* WELCOME TO THE DICE ROLLER *=-=-=-=*
----------------------------------------------""")
wel_lab.pack()

L1 = Label(top, text="Do you wanna roll a die?")
L1.pack()
B1 = Button(top, text="Yes", command=dice_roll)
B1.pack()
B2 = Button(top, text="No", command=exit)
B2.pack()
L3 = Label(top, text=f"You rolled: {display}")
L3.pack()

SB1 = Spinbox(top, from_=1, to=10)
SB1.pack(side=BOTTOM)
L2 = Label(top, text="How many dice?")
L2.pack(side=BOTTOM)


top.mainloop()
