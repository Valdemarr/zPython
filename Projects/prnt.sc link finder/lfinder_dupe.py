from tkinter import *
import webbrowser
import random
import os

# VARIABLES
url_start = "https://prnt.sc/"
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
           "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
font = "Roboto"
white = "#FFFFFF"

# DRAWING WINDOW and structure
window = Tk()
window.geometry("600x350")
window.title("LightShot Link Finder")
window.configure(bg='#FFFFFF')
frame1 = Frame(window, bg=white)
frame1.pack(expand=True)
frame2 = Frame(window, bg=white)
frame2.pack(expand=True)
frame3 = Frame(window, bg=white)
frame3.pack(expand=True)

# FUNCTION DOING THE ACTUAL THING


def find_link():
    result = ""

    # STANDARD 2 LETTERS 4 NUMBERS FIND
    if var1.get() == 0:
        for i in range(2):
            result += random.choice(letters)

        for i in range(4):
            result += random.choice(numbers)
    # NUMBERS ONLY OPTION
    if var1.get() == 1:
        for i in range(6):
            result += random.choice(letters)

    webbrowser.open_new(url_start+result)

    # DYNAMIC TEXT IN WINDOW SHOWING MOST RECENT LINK FOUND
    L3.configure(text=f"Most recent link: {url_start+result}")

    # WRITE LINK HISTORY
    f = open(r"G:\Mit drev\Rayndom\zPython\Projects\prnt.sc link finder\prnt.sc links.txt", "a")
    f.write(str(f"{url_start+result}\n"))
    f.close()

    # JUST A COMMAND LINE UPDATE - NOT IMPORTANT
    print(url_start + result)


def open_folder():
    os.startfile(
        r"G:\Mit drev\Rayndom\zPython\Projects\prnt.sc link finder\prnt.sc links.txt", "open")


# GUI elements
L1 = Label(frame1, text="Click to find new link", font=font, bg=white)
L1.pack(expand=True)

B1 = Button(frame2, text="Find link", command=find_link,
            height=3, width=20, bg="#8B6FA6", font=font, fg=white)
B1.pack(expand=True, side=LEFT)

var1 = IntVar()
CB1 = Checkbutton(frame2, text="Use only letters", variable=var1,
                  onvalue=1, offvalue=0, font=font, bg=white)
CB1.pack(expand=True, side=RIGHT)

L3 = Label(frame3, text="Most recent link: None yet", font=font, bg=white)
L3.pack(expand=True, side=LEFT)

B2 = Button(frame3, text="Open link history", command=open_folder, font=font, bg=white)
B2.pack(expand=True, side=RIGHT)

# NECESSARY TO DRAW WINDOW
window.mainloop()
