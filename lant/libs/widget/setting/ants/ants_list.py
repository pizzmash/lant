import tkinter
import tkinter.ttk
from typing import List
from libs.domain.ant import Ant
from libs.domain.position import Position
from libs.domain.direction import Direction


class AntsListWidget(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        self.listbox = tkinter.Listbox(self, width=20, height=5)
        self.listbox.grid(row=0, column=0)
        
        scrollbar = tkinter.Scrollbar(self,
                                      orient=tkinter.VERTICAL,
                                      command=self.listbox.yview)
        self.listbox['yscrollcommand'] = scrollbar.set
        scrollbar.grid(row=0, column=1, sticky=(tkinter.N, tkinter.S))
        
        self.ants: List[Ant] = []
    
    def set(self, pos_x: int, pos_y: int, direction: str):
        directionStateMapper = {
            "North": Direction.State.NORTH,
            "East": Direction.State.EAST,
            "South": Direction.State.SOUTH,
            "West": Direction.State.WEST
        }
        self.ants.append(Ant(Position(pos_x, pos_y), Direction(directionStateMapper[direction])))
        
        value = "x:{}, y:{}, d:{}".format(pos_x, pos_y, direction)
        self.listbox.insert(tkinter.END, value)
