from enum import Enum
from typing import List
from lant.libs.domain.position import Position


class Field:
    class TurnDirection(Enum):
        LEFT = 0
        RIGHT = 1
    
    def __init__(self, states: List['Field.TurnDirection']) -> None:
        if len(states) == 0:
            raise ValueError() 
        self.states = states
        self.state_map = {}
    
    def update_at(self, position: Position):
        if position.to_tuple() not in self.state_map:
            self.state_map[position.to_tuple()] = 0
        else:
            self.state_map[position.to_tuple()] = (self.state_map[position.to_tuple()] + 1) % len(self.states)
    