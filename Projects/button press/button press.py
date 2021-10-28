from tkinter import *

# VARIABLES


# GUI VARIABLES
font = "Roboto"
white = "#FFFFFF"
H1 = "H1 title"
button_text = "Button text"
main_color = "#6EA8E4"

# DRAWING WINDOW and structure
window = Tk()
window.geometry("600x300")
window.title("Window title")
window.configure(bg='#FFFFFF')
frame1 = Frame(window, bg=white)
frame1.pack(expand=True)
frame2 = Frame(window, bg=white)
frame2.pack(expand=True)
frame3 = Frame(window, bg=white)
frame3.pack(expand=True)
frame4 = Frame(window, bg=white)
frame4.pack(expand=True)

# FUNCTION DOING THE ACTUAL THING


def action():
    a = var1.get()
    b = a+1

    L3.config(text=f"Button pressed {b} times")
    var1.set(b)

    file = open(r"G:\Mit drev\Rayndom\zPython\Projects\button press\number.txt", "w")
    file.write(str(b))
    file.close()

    number_change = open(r"G:\Mit drev\Rayndom\zPython\Projects\button press\number_perm.txt", "w")

    a2 = var2.get()

    b2 = a2 + 1

    num = int(number) + 1

    L4.config(text=f"testa: {b2}")
    # var2.set(b2)
    # JUST A COMMAND LINE UPDATE - NOT IMPORTANT
    print(f"number: {number}")
    print(f"a2: {a2}")

    number_change.write(str(b2))
    number_change.close()

    print(f"b2: {b2}")


def action2():
    pass


var1 = IntVar()
var2 = IntVar()
# GUI elements
L1 = Label(frame1, text=H1, font=font, bg=white)
L1.pack(expand=True)

B1 = Button(frame2, text=button_text, command=action,
            height=3, width=20, bg=main_color, font=font, fg=white)
B1.pack(expand=True, side=LEFT)
#
#var1 = IntVar()
#CB1 = Checkbutton(frame2, text="Use only letters", variable=var1, onvalue=1, offvalue=0, font=font, bg=white)
#CB1.pack(expand=True, side=RIGHT)

L3 = Label(frame3, text=f"Button pressed 0 times", font=font, bg=white)
L3.pack(expand=True, side=LEFT)

open_number = open(r"G:\Mit drev\Rayndom\zPython\Projects\button press\number_perm.txt", "r")
number = open_number.readline()
open_number.close()

L4 = Label(frame4, text=f"test: {number}", font=font, bg=white)
L4.pack(expand=True, side=RIGHT)

#B2 = Button(frame3, text="Open link history", command=action2, font=font, bg=white)
#B2.pack(expand=True, side=RIGHT)

# NECESSARY TO DRAW WINDOW
window.mainloop()
