import tkinter
from typing import List
from libs.util.simlator import Simulator
from libs.widget.canvas.core import CanvasWidget


class CanvasApp:
    def __init__(self,
                 simulator: Simulator,
                 size: int,
                 plus_minus_range: int,
                 ants_color: str,
                 bg_color: str,
                 field_states_colors: List[str]):
        root = tkinter.Tk()
        root.title("Langton's ant")
        self.app = CanvasWidget(root, simulator, size, plus_minus_range, ants_color, bg_color, field_states_colors)
    
    def run(self):
        self.app.mainloop()
