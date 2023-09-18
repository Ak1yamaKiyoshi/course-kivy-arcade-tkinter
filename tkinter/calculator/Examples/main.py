import tkinter, os, random

colors = ['Green', 'Red', 'Blue','Yellow', 'Pink', 'Orange', 'Purple', 'Grey', 'Brown', 'Black']

window = tkinter.Tk()
os.chdir(os.path.dirname(os.path.abspath(__file__)))


def populateMethod(method):
    print ("method:", method)

def color(color):
    colors.remove(color)
    text = random.choice(colors)
    label = tkinter.Label(window, text=color, fg = text, highlightthickness = 20)
    label.config(font=("Calibri", 44))
    buttonT = tkinter.Button(window, text=text,command=lambda m=text: populateMethod(m))
    buttonF = tkinter.Button(window, text=color,command=lambda m=color: populateMethod(m))
    colors.append(color)
    label.pack()
    buttonT.pack()
    buttonF.pack()

os.chdir(os.path.dirname(os.path.abspath(__file__)))

window.title('Color Game')
window.geometry('250x250')
instructions = tkinter.Label(window, text = 'Select word, not color!')
instructions.pack()
# window.iconbitmap('icon.ico')
color(random.choice(colors))

window.mainloop()