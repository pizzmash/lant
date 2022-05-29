import math
import tkinter
from typing import List
from libs.domain.position import Position


class FieldCanvas(tkinter.Canvas):
    def __init__(self,
                 master,
                 size: int,
                 plus_minus_range: int,
                 ants_color: str,
                 bg_color: str,
                 field_states_colors: List[str]):
        
        super().__init__(master, width=size, height=size)

        self.size = size
        self.plus_minus_range = plus_minus_range
        self.ants_color = ants_color
        self.bg_color = bg_color
        self.field_states_colors = field_states_colors
        self.mass_size = math.ceil(size/(plus_minus_range*2))
    
    
    def setup(self):
        self.create_rectangle(0,
                              0,
                              self.size,
                              self.size,
                              fill=self.bg_color,
                              width=0)
    
    def start_pos_of(self, position_value: int):
        start_pos = position_value + self.plus_minus_range
        start_pos *= self.size / self.plus_minus_range / 2.
        return round(start_pos)
    
    def draw_states(self, positions: List[Position], states: List[int]):
        for (position, state) in zip(positions, states):
            start_pos_x = self.start_pos_of(position.pos_x)
            start_pos_y = self.start_pos_of(-position.pos_y)
            self.create_rectangle(start_pos_x,
                                  start_pos_y,
                                  start_pos_x + self.mass_size,
                                  start_pos_y + self.mass_size,
                                  fill=self.field_states_colors[state],
                                  width=0)
    
    def draw_ants(self, positions: List[Position]):
        for position in positions:
            start_pos_x = self.start_pos_of(position.pos_x)
            start_pos_y = self.start_pos_of(-position.pos_y)
            self.create_rectangle(start_pos_x,
                                  start_pos_y,
                                  start_pos_x + self.mass_size,
                                  start_pos_y + self.mass_size,
                                  fill=self.ants_color,
                                  width=0)
