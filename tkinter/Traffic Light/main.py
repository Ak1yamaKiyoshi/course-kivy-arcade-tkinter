from tkinter import *

class App:
    def __init__(self) -> None:
        self.root = Tk()
        self.root.geometry("200x300")
        self.root.title("Traffic Light")

        main_frame = Frame(self.root, background="gray", width=200, height=300, padx=10, pady=10)
        main_frame.pack()

        self.redButton = Button(main_frame, width=10, height=5, background="#960000", highlightthickness=0, relief="flat", command=lambda: self.switchDarkBright(0))
        self.redButton.pack()
        self.yellowButton = Button(main_frame, width=10, height=5, background="#969100",highlightthickness=0, relief="flat",command=lambda: self.switchDarkBright(1) )
        self.yellowButton.pack()
        self.greenButton = Button(main_frame, width=10, height=5, background="#0d9c00", highlightthickness=0, relief="flat", command=lambda: self.switchDarkBright(2))
        self.greenButton.pack()
        
        self.buttons = [self.redButton, self.yellowButton, self.greenButton]

        main_frame1 = Frame(self.root, background="gray", width=200, height=300, padx=10, pady=10)
        main_frame1.pack()

        #self.AredButton = Button(main_frame1,background="#960000", highlightthickness=0, relief="flat", command=lambda: self.switchA(0) )
        #self.AredButton.pack()
        #self.AyellowButton = Button(main_frame1,background="#969100",highlightthickness=0, relief="flat", command=lambda: self.switchA(1) )
        #self.AyellowButton.pack()
        #self.AgreenButton = Button(main_frame1, background="#0d9c00", highlightthickness=0, relief="flat", command=lambda: self.switchA(2) )
        #self.AgreenButton.pack()
        
        #self.Abuttons = [self.AredButton, self.AyellowButton, self.AgreenButton]

        self.root.mainloop()

    def switchDarkBright(self, i):
        colors = {
            0: ["#ff0000", "#960000"], 
            1: ["#fff700", "#969100"],
            2: ["#15ff00", "#0d9c00"]
        }

        if i > 0 and self.buttons[i-1].cget('bg') == colors[i-1][0] and self.buttons[2].cget('bg') != colors[2][0] or i == 0 and self.buttons[2].cget('bg') != colors[2][0]:
            self.buttons[i].configure(bg=colors[i][0])
        elif self.buttons[2].cget('bg') == colors[2][0]:
            for j in range(3):
                self.buttons[j].configure(bg=colors[j][1])

    def switchA(self, i):
        colors = {
            0: ["#ff0000", "#960000"], 
            1: ["#fff700", "#969100"],
            2: ["#15ff00", "#0d9c00"]
        }

        if i > 0 and self.Abuttons[i-1].cget('bg') == colors[i-1][0] and self.Abuttons[2].cget('bg') != colors[2][0] or i == 0 and self.Abuttons[2].cget('bg') != colors[2][0]:
            self.Abuttons[i].configure(bg=colors[i][0])
        elif self.Abuttons[2].cget('bg') == colors[2][0]:
            for j in range(3):
                self.Abuttons[j].configure(bg=colors[j][1])
        if i < 2:
            self.root.after(200, lambda: self.switchA(i+1))
        else:
            self.root.after(200, lambda: self.switchA(0))

App()