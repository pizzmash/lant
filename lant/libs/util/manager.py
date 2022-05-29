from typing import List
from libs.util.simlator import Simulator
from libs.widget.canvas.field_canvas import FieldCanvas

class Manager:
    def __init__(self, simulator: Simulator, canvas: FieldCanvas):
        self.simulator = simulator
        self.canvas = canvas
    
    def setup(self):
        self.canvas.setup()
        ant_positions = [ant.position for ant in self.simulator.ants]
        self.canvas.draw_ants(ant_positions)
    
    def forward(self):
        pre_ant_positions = [ant.position for ant in self.simulator.ants]
        pre_states = [self.simulator.field.state_map[position.to_tuple()] for position in pre_ant_positions]
        self.canvas.draw_states(pre_ant_positions, pre_states)
        
        self.simulator.forward()
        
        new_ant_positions = [ant.position for ant in self.simulator.ants]
        self.canvas.draw_ants(new_ant_positions)
