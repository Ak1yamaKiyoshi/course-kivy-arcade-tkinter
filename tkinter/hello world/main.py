from tkinter import *
from tkinter import ttk


def hello():
    ttk.Label(frm, text="Hello World!").grid(column=0, row=1)

# root window
root = Tk()
root.geometry("100x100")
root.resizable(False, False)
root.title("Hello World")

# Frame 
frm = ttk.Frame(root, padding=10)
frm.grid()

ttk.Button(frm, text="Hello World", command=hello).grid(column=0, row=0)
ttk.Button(frm, text="Exit", command=root.destroy).grid(column=0, row=2)

root.mainloop()