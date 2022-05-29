import re
import tkinter
import tkinter.ttk
from typing import List
from libs.domain.ant import Ant
from libs.widget.setting.ants.ants_list import AntsListWidget
from libs.widget.setting.ants.direction_select import DirectionSelectWidget
from libs.widget.setting.validation_form import ValidationFormWidget


class AntsWidget(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master, borderwidth=2, relief="raised")
        
        validater = lambda value: re.match(r'^[+|-]?\d$', value)
        self.pos_x_entry_widget = ValidationFormWidget(self,
                                                       validater=validater,
                                                       label_text='x pos: ',
                                                       entry_width=6,
                                                       is_horizontal=True)
        self.pos_x_entry_widget.grid(row=0, column=0, padx=3, pady=5)
        self.pos_y_entry_widget = ValidationFormWidget(self,
                                                       validater=validater,
                                                       label_text='y pos: ',
                                                       entry_width=6,
                                                       is_horizontal=True)
        self.pos_y_entry_widget.grid(row=0, column=1, padx=3, pady=5)
        
        self.direction_select_widget = DirectionSelectWidget(self)
        self.direction_select_widget.grid(row=1,
                                          column=0,
                                          columnspan=2,
                                          padx=5, pady=5,
                                          sticky=tkinter.W)
        
        button = tkinter.Button(self, text="Add a Ant")
        button.bind("<Button-1>", self.regist)
        button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
        
        self.ants_list_widget = AntsListWidget(self)
        self.ants_list_widget.grid(row=0, column=2, rowspan=3, columnspan=2, padx=5, pady=5)

    def regist(self, event):
        pos_x_str = self.pos_x_entry_widget.validate_and_get()
        pos_y_str = self.pos_y_entry_widget.validate_and_get()
        if pos_x_str is None or pos_y_str is None:
            return
        else:
            direction= self.direction_select_widget.get()
            self.ants_list_widget.set(int(pos_x_str), int(pos_y_str), direction)
    
    def getAnts(self) -> List[Ant]:
        return self.ants_list_widget.ants
