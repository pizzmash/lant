import re
import tkinter

from libs.domain.field import Field
from libs.domain.manager import Manager
from libs.widget.setting.validation_form import ValidationFormWidget
from libs.widget.setting.ants.core import AntsWidget


class SettingWidget(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid()
        
        validater = lambda value: re.match(r'^(L|R)+$', value)
        self.pattern_widget = ValidationFormWidget(self,
                                                   validater=validater,
                                                   label_text="Movement pattern: ",
                                                   entry_width=36,
                                                   is_horizontal=True)
        self.pattern_widget.grid(row=0, column=0, padx=5, pady=5)
        
        self.ants_widget = AntsWidget(self)
        self.ants_widget.grid(row=1, column=0, padx=5, pady=5)
        
        button = tkinter.Button(self, text="Simulate")
        button.bind("<Button-1>", self.setup)
        button.grid(row=2, column=0, pady=5)
    
    def setup(self, event):
        pattern = self.pattern_widget.validate_and_get()
        ants = self.ants_widget.getAnts()
        
        if pattern is None or len(ants) == 0:
            return
        else:
            states = [Field.TurnDirection.LEFT if ch == 'L' else Field.TurnDirection.RIGHT for ch in pattern]
            self.generated_manager = Manager(Field(states), ants)
            self.quit()
            return
