import tkinter


class ValidationFormWidget(tkinter.Frame):
    def __init__(self, master,
                 validater,
                 label_text: str,
                 entry_width: int,
                 is_horizontal: bool=True):
        super().__init__(master)
        
        self.validater = validater
        
        label = tkinter.Label(self, text=label_text)
        label.grid(row=0,
                   column=0,
                   sticky=tkinter.E if is_horizontal else tkinter.W)
        
        self.entry = tkinter.Entry(self, width=entry_width)
        self.entry.grid(row=0 if is_horizontal else 1,
                        column=1 if is_horizontal else 0,
                        sticky=tkinter.W)

    def validate_and_get(self):
        if self.validater(self.entry.get()):
            self.change_color(True)
            return self.entry.get()
        else:
            return self.change_color(False)

    def change_color(self, is_valid):
        self.entry.configure(bg="#FFFFFF" if is_valid else "#FF8080")
