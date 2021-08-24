from tkinter import *
from tkinter import messagebox

window = Tk()

window.title("Login Form")
window.geometry("500x500")
window.config(bg="")

# Defining functions

username = ["Aaliyah", "Thabo", "Mujaid", "Ayyoob"]
key = ["1111", "2222", "3333", "4444"]


def membership():

    for x in range(len(key)):
        if name_entry.get() == username[x] and password_entry.get() == key[x]:
            found = True
            if found == True:
                messagebox.showinfo(title="Status", message="Access Granted!")
                window.destroy()
                import Lotto
        else:
            messagebox.showerror(title="Error", message="Access Denied!")
            window.destroy()


def clear_btn():
    name_entry.delete(0, END)
    password_entry.delete(0, END)


def exit_btn():
    return window.destroy()


# Frame
myframe = Frame(window)
myframe.place(x=10, y=10, width=500, height=500)

# Labels
name = Label(myframe, text="Username: ")
name.place(x=20, y=20)
password = Label(myframe, text="Password: ")
password.place(x=20, y=50)

# Entry
name_entry = Entry(myframe)
name_entry.place(x=110, y=20)
password_entry = Entry(myframe, show="*")
password_entry.place(x=110, y=50)

# Button
verify = Button(myframe, text="Login", command=membership)
verify.place(x=30, y=150)
clear = Button(myframe, text="Clear", command=clear_btn)
clear.place(x=100, y=150)
fin = Button(myframe, text="Exit", command=exit_btn)
fin.place(x=170, y=150)

window.mainloop()
