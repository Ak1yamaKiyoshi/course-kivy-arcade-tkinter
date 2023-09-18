#import tkinter as tk
from tkinter import *

class App:
    def __init__(self):
        # __root
        self.__root = Tk()
        self.__root.title("Test tkinter")
        self.__root.resizable(False, False)
        self.__root.geometry("375x250")
        # __frm_right, 
        self.__frm_right = Frame(self.__root,  height=200, width=200)
        self.__frm_right.grid(column=1, row=0, sticky="n")
        # left frame 
        self.__frm_left = Frame(
            self.__root, 
            height=250, 
            width=100, 
            pady=5, 
            padx=5, 
            bg="white", 
            border=4,
            relief="groove"
        )
        self.__frm_left.grid(column=0, row=0, sticky="n")
        
        self.__rbtn_menu = StringVar() # Radio button group variable 
        radio_buttons_values = { # Radio button keys
            "Radiobuttons":"radiobutton",
            "Checkboxes":"checkbox", 
            "Other":"other", 
        }
        
        Label(self.__frm_left, text="What to watch").grid(column=0, row=0, sticky="w")
        # Radiobuttons 
        left_rbtn_ind=1;
        for (text, value) in radio_buttons_values.items():
            Radiobutton(
                self.__frm_left, 
                highlightthickness=0,
                variable = self.__rbtn_menu, 
                value=value, 
                text=text, 
                bg="white"
            ).grid(column=0, row=left_rbtn_ind, sticky="w")
            left_rbtn_ind+=1
        # Button to process radiobuttons variable __rbtn_menu
        Button(
                self.__frm_left, 
                text="process", 
                command=self.draw_right_frame
            ).grid(column=0, row=4, sticky="w")
        # Label that tells which variant user have chosen
        self.__lbl_chosen_rbtn = Label(self.__frm_left, text="", bg="white")
        self.__lbl_chosen_rbtn.grid(column=0, row=5, sticky="w")
        
        self.__root.mainloop()
        
    def draw_right_frame(self):
        # Change label with chosen variant
        self.__lbl_chosen_rbtn.configure(text="chosen variant:\n"+self.__rbtn_menu.get())
        # Redraw right frame
        self.__frm_right.destroy()
        self.__frm_right = Frame(
            self.__root,  
            height=200, 
            width=200, 
            border=4, 
            padx=10, 
            pady=10,
            relief="groove"
        )
        self.__frm_right.grid(column=1, row=0, sticky="n")
        
        # Radiobutton frame 
        if (self.__rbtn_menu.get() == "radiobutton"):
            right_rbtn_ind=1; # index for radiobuttons
            self.__right_rbtn_food = StringVar() # radiobuttons variable
            radio_buttons_values = { # radiobuttons keys
                "Pizza":"pizza",
                "Hamburger":"hamburger", 
                "Olives":"olive", 
                "Banans":"banana",
                "Cucumbers":"cucumber"
            }
    
            Label(
                self.__frm_right, 
                text="Radiobuttons\n choose what do you like"
                ).grid(column=0, row=0, sticky="w")
            # Radiobutton group with food
            for (text, value) in radio_buttons_values.items():
                Radiobutton(
                    self.__frm_right, 
                    text=text, 
                    variable=self.__right_rbtn_food, 
                    value=value
                ).grid(column=0, row=right_rbtn_ind, sticky="w")
                right_rbtn_ind+=1
            
            # label that shows current chosen variant 
            self.__right_lbl_rdbtn_food = Label(self.__frm_right, text="  You like: \n")
            self.__right_lbl_rdbtn_food.grid(column=0, row=6, sticky="w")
            
            Button(
                self.__frm_right, 
                text="process", 
                command=self.__right_rdbtns_food
            ).grid(column=0, row=7, sticky="w")
        
        # Checkbox frame 
        elif self.__rbtn_menu.get() == "checkbox":
            self.__right_chckbx_bg= IntVar() # checkbox value for background change
            self.__right_chckbx_style= IntVar() # checkbox value for border style change
            self.__chckbx_frame_list = [] # list of all elements in checkbox frame
            
            self.__chckbx_frame_list.append(
                Label(self.__frm_right, text="Checkbuttons", highlightthickness=0)
            )
            self.__chckbx_frame_list[-1].grid(column=0, row=0, sticky="w")
            self.__chckbx_frame_list.append(
                    Checkbutton(
                        self.__frm_right, 
                        text="change bg to white", 
                        variable=self.__right_chckbx_bg, 
                        highlightthickness=0
                    )
                )
            self.__chckbx_frame_list[-1].grid(column=0, row=1, sticky="w")
            self.__chckbx_frame_list.append(
                    Checkbutton(
                        self.__frm_right, 
                        text="change border of main menu", 
                        variable=self.__right_chckbx_style, 
                        highlightthickness=0
                    )
                )
            self.__chckbx_frame_list[-1].grid(column=0, row=2, sticky="w")
            self.__chckbx_frame_list.append(
                    Button(
                        self.__frm_right, 
                        text="process", 
                        command=self.__right_chckbx_style_bg, 
                        highlightthickness=0
                    )
                )
            self.__chckbx_frame_list[-1].grid(column=0, row=3, sticky="w")
        
        # Entry frame 
        elif self.__rbtn_menu.get() == "other":
            self.__right_entry = Entry(self.__frm_right)
            self.__right_entry.grid(column=0, row=0, sticky="w") 
            # Entry label
            self.__right_lbl_entry = Label(self.__frm_right, text="Your message will be here")
            self.__right_lbl_entry.grid(column=0, row=1, sticky="w")
            Button(self.__frm_right, text="show message", command=self.__right_entry_show_message).grid(column=0, row=2, sticky="w") 
            
            
    def __right_entry_show_message(self):
        self.__right_lbl_entry.configure(text=self.__right_entry.get())
    def __right_rdbtns_food(self):
        # Radiobuttons label with current variant change text 
        self.__right_lbl_rdbtn_food.configure(text="  You like: \n"+self.__right_rbtn_food.get())
        
    def __right_chckbx_style_bg(self):
        # change background of checkbuttons frame to white
        # and all elements on this frame too
        if self.__right_chckbx_bg.get() == 1:
            self.__frm_right.configure(background="white")
            for i in range(len(self.__chckbx_frame_list)):
                self.__chckbx_frame_list[i].configure(background="white")
        else:
            # make it default color 
            self.__frm_right.configure(background="gainsboro")
            for i in range(len(self.__chckbx_frame_list)):
                self.__chckbx_frame_list[i].configure(background="gainsboro")
        # chabge style of left radiobutton menu
        if self.__right_chckbx_style.get() == 1:
            self.__frm_left.configure(relief='solid')
        else:
            self.__frm_left.configure(relief='groove')

if __name__ == "__main__":
    App()