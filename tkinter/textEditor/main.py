from tkinter import *
from tkinter import filedialog as fd
from tkinter import scrolledtext

class App():
    def __init__(self) -> None:
        
        def select_all(event):
            self.txtbx_field.tag_add(SEL, "1.0", END)
            self.txtbx_field.mark_set(INSERT, "1.0")
            self.txtbx_field.see(INSERT)
            self.update_size(event)
            return 'break'
        
        def copy(event):
            self.txtbx_field.selection_get()
            self.update_size(event)
        
        def paste(event):
            self.txtbx_field.insert(1.0, self.root.clipboard_get())
            self.update_size(event)
        
        self.root = Tk()
        self.root.geometry("366x380")
        self.root.resizable(True, True)
        self.root.title("Text Editor")
        
        self.root.rowconfigure(1, weight=1)
        self.root.columnconfigure(0, weight=1)
        
        frm_panel = Frame(self.root, background="#ffffff", width=400, height=50) 
        frm_panel.grid(row=0, column=0)
            

        frm_text = Frame(self.root, background="#e6e6e6", width=400, height=350) 
        frm_text.grid(row=1, column=0)
        frm_text.rowconfigure(0, weight=1)

        #self.fieldT = Text(dataF, width=45, background="#e6e6e6", relief="flat", height=20)
        self.txtbx_field = scrolledtext.ScrolledText(frm_text, width=45, background="#e6e6e6", relief="flat", height=20)
        self.txtbx_field.grid(column=0, row=0, sticky=E+W+N+S)
        self.txtbx_field.bind('<Control-Key-a>', select_all)
        self.txtbx_field.bind('<Control-Key-A>', select_all)
        
        self.txtbx_field.bind('<Control-Key-c>', copy)
        self.txtbx_field.bind('<Control-Key-C>', copy)
        
        self.txtbx_field.bind('<Control-Key-v>', paste)
        self.txtbx_field.bind('<Control-Key-V>', paste)
        self.root.bind("<Configure>", self.update_size)
        
                
        # Panel buttons 
        buttons = {
            "Save file": self.saveFile,
            "Open file": self.openFile            
        }
        
        for i, (text, command) in enumerate(buttons.items()):
            Button(frm_panel, text=text, command=command, height=1, relief="flat", background="#e6e6e6", highlightbackground="#696969", highlightthickness=0.5).grid(column=i, row=0)
         
        
        self.root.update()
        self.root.mainloop()    
    
    def update_size(self, event):
        widget_width = int((self.root.winfo_width() )/8.35)
        widget_height = int((self.root.winfo_height()-100 )/8.35)
        print(widget_width, widget_height)
        self.txtbx_field.config(width=widget_width, height=widget_height)
    
    def saveFile(self):
        data = self.txtbx_field.get(1.0, "end-1c")
        file = fd.asksaveasfile(initialfile = 'Untitled.txt', defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        file.write(data)
        file.close() 
        
    def openFile(self):
        path = fd.askopenfilename()
        with open(path) as file:
            self.txtbx_field.delete(1.0, "end-1c")
            self.txtbx_field.insert(1.0, file.read())
    
App()