from tkinter import *

# VARIABLES
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

# FUNCTION DOING THE ACTUAL THING


def action():
    a = var1.get()
    b = a+1

    L3.config(text=f"Button pressed {b} times")

    var1.set(b)
    # JUST A COMMAND LINE UPDATE - NOT IMPORTANT
    print(b)

    file = open(r"G:\Mit drev\Rayndom\zPython\Projects\button press\number.txt", "w")
    file.write(str(b))
    file.close()


def action2():
    pass


var1 = IntVar()
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

L3 = Label(frame3, text=f"Button pressed{var1}", font=font, bg=white)
L3.pack(expand=True, side=LEFT)

#B2 = Button(frame3, text="Open link history", command=action2, font=font, bg=white)
#B2.pack(expand=True, side=RIGHT)

# NECESSARY TO DRAW WINDOW
window.mainloop()
