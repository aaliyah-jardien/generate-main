import random
from tkinter import *

root = Tk()
root.title("Lotto")
root.geometry("500x500")
root.config(bg="black")
# Generate five random numbers
# Numbers must not repeat
# Numbers must be sorted

def gen_num():
    x = 0
    y = []
    while x < 6:
        r = random.randint(1, 42)
        if r not in y:
            y.append(r)
            x = x + 1
    else:
        x = x - 1
    y.sort()
    labl_text.set(y)

title = Label(root, text="Lotto")
title.place(x=350, y=10)
title.config(bg="red")

labl_text = StringVar()
lab1 = Label(root, text="Generate 5 random numbers: ", bg="red")
lab1.place(x=10, y=100)
lab2 = Label(root, text="", textvariable=labl_text)
lab2.place(x=250, y=100)

b1 = Button(root, text="Generate", command=gen_num, bg="red")
b1.place(x=10, y=300)

root.mainloop()
