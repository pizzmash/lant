import threading
import time
import tkinter
from typing import List
from libs.util.manager import Manager
from libs.util.simlator import Simulator
from libs.widget.canvas.field_canvas import FieldCanvas


class CanvasWidget(tkinter.Frame):
    def __init__(self,
                 master,
                 simulator: Simulator,
                 size: int,
                 plus_minus_range: int,
                 ants_color: str,
                 bg_color: str,
                 field_states_colors: List[str],
                 sleep_time=0.):
        super().__init__(master)
        self.grid()
        
        self.sleep_time = sleep_time
        
        canvas = FieldCanvas(self, size, plus_minus_range, ants_color, bg_color, field_states_colors)
        canvas.grid(row=0, column=0)
        
        self.manager = Manager(simulator, canvas)
        self.manager.setup()
        self.thread = threading.Thread(target=self.process)
        self.thread.daemon = True
        self.thread.start()
    
    def process(self):
        while True:
            if self.sleep_time != 0.:
                time.sleep(self.sleep_time)
            self.manager.forward()
