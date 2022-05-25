from enum import Enum
from lant.libs.domain.position import Position


class Field:
    class State(Enum):
        UNREACHED = 0
        REACHED = 1
    
    def __init__(self, width: int, height: int) -> None:
        if width <= 0:
            raise ValueError("Invalid value. width={}".format(width))
        if height <= 0:
            raise ValueError("Invalid value. height={}".format(height))
        
        self.states = [[self.State.UNREACHED for _ in range(width)] for _ in range(height)]
    
    def update_at(self, position: Position):
        self.states[position.pos_x][position.pos_y] = Field.State((self.states[position.pos_x][position.pos_y].value + 1) % len(Field.State))
    