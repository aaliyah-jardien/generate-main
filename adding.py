from tkinter import *
from tkinter import messagebox
# Add two numbers tkinter exercise

def addition():
    try:
        myanswer = int(e1.get()) + int(e2.get())
        lab3.config(bg="#ffffff", width=20)
        label_text.set(myanswer)
    except ValueError:
        if e1.get() != int:
            messagebox.showerror(title="Status", message="Invalid! Please enter an integer")


def clear_btn():
    e1.delete(0, END)
    e2.delete(0, END)
    label_text.set("")
    lab3.config(bg="#222222")


def exit_btn():
    return root.destroy()


root = Tk()

root.title("Adding two numbers")
root.geometry("500x500")
root.config(bg="#222222")

label_text = StringVar()
lab1 = Label(root, text="Please enter first number: ")
lab1.place(x=10, y=10)
lab2 = Label(root, text="Please enter second number: ")
lab2.place(x=10, y=50)
lab3 = Label(root, text="", textvariable=label_text, bg="#222222")
lab3.place(x=210, y=85)

e1 = Entry(root)
e1.place(x=210, y=10)
e2 = Entry(root)
e2.place(x=210, y=50)

b1 = Button(root, text="Add", command=addition)
b1.place(x=10, y=150)
clear = Button(root, text="Clear", command=clear_btn)
clear.place(x=75, y=150)
leave = Button(root, text="Exit", command=exit_btn)
leave.place(x=150, y=150)

root.mainloop()
