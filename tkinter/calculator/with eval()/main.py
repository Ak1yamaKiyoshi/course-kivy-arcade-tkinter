from tkinter import *
import re

class App():
    def __init__(self):
        root = Tk()
        root.geometry("300x300")
        root.title("Calculator")

        main_frame = Frame(root, background="blue", width=100, height=100, padx=10, pady=10)
        main_frame.grid(row=0, column=0)

        self.__example_field = Entry(main_frame, background="white", width=18, highlightthickness=0)
        self.__example_field.grid(row=0, column=0)

        buttons_frame = Frame(main_frame, width=30)
        buttons_frame.grid(row=1, column=0)

        number_buttons = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0","(",")","+","-","*","/"]
        y, x = 1, 1
        for txt in number_buttons:
            Button(buttons_frame, text=txt, highlightthickness=0, relief="flat", width=3,
            command= lambda m=txt: self.add_txt(m)).grid(row=y, column=x)
            if (x == 3):
                x = 0
                y += 1
            x+=1 

        Button(buttons_frame, text="x", highlightthickness=0, relief="flat",
            command=lambda: self.erase_txt(), 
        ).grid(row=6, column=2)
        Button(buttons_frame, text="=", highlightthickness=0, relief="flat",
            command= self.calculate, 
        ).grid(row=6, column=3)

        root.mainloop()

    def add_txt(self, text):
        operations = ["+","-","*","/"]
        if len(self.__example_field.get()) > 0:
            if self.__example_field.get()[-1] in operations and text in operations:
                return
            if self.__example_field.get()[-1] == "0" and text not in operations:
                return
        self.__example_field.insert(self.__example_field.index("end"), text)

    def erase_txt(self, eraseall=0):
        if eraseall==0:
            self.__example_field.delete(self.__example_field.index("end") - 1)
        else:
            self.__example_field.delete(0, self.__example_field.index("end"))

    def validation(self):
        if len(re.findall("[^0-9+-=()*/]", self.__example_field.get())) > 0:
            return False
        return True

    def calculate(self):
        if self.validation() == False or self.__example_field.get == "error":
            self.erase_txt(1)
            self.add_txt("error")

        expression = self.__example_field.get()
        self.erase_txt(1)
        self.add_txt(str(eval(expression)))

App()
