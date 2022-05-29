import tkinter


class DirectionSelectWidget(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        label = tkinter.Label(self, text="Initial direction: ")
        label.grid(row=0, column=0, sticky=tkinter.E)
        
        directions = ('North', 'East', 'South', 'West')
        self.string_var = tkinter.StringVar()
        combobox = tkinter.ttk.Combobox(self,
                                        values=directions,
                                        textvariable=self.string_var,
                                        width=7,
                                        state="readonly")
        combobox.current(0)
        combobox.grid(row=0, column=1, sticky=tkinter.W)
    
    def get(self):
        return self.string_var.get()
